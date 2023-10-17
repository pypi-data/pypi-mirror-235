import logging
import sys
from datetime import datetime
import os
import threading
import queue
import atexit
from typing import Union

from sqlalchemy import MetaData, Table
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.ext.declarative

from .conf import _LoggingConf
from .models import LoggerFrame
from ._tables import get_columns

_metadata = MetaData()
logs_table: Union[Table, None] = None


class DBTaskManager:
    """
    Manages a queue of tasks that need to be executed in separate threads.

    Attributes:
        queue (queue.Queue): A thread-safe queue for storing tasks.
        lock (threading.Lock): A lock to protect shared resources.
        process_thread (threading.Thread | None): The thread responsible for processing tasks.

    Methods:
        submit_thread(target, args): Submit a task to the queue for execution.
        process_queue(): Continuously process tasks from the queue in a separate thread.
        start(): Start the thread for processing tasks.
        stop(): Stop the thread for processing tasks.
    """

    def __init__(self):
        """
        Initialize a DBTaskManager instance.

        This constructor initializes a DBTaskManager instance and sets up a queue, a lock, and a processing thread.
        """
        self.queue = queue.Queue()
        self.lock = threading.Lock()
        self.process_thread = None

    def submit_thread(self, target, args):
        """
        Submit a new thread for execution.

        Args:
            target (callable): The target function to run in the new thread.
            args (tuple): The arguments to pass to the target function.

        This method adds a new thread with the specified target function and arguments to the queue. If the processing
        thread is not running, it starts the processing thread.
        """
        self.queue.put((target, args))
        if self.process_thread is None or not self.process_thread.is_alive():
            self.start()

    def process_queue(self):
        """
        Process threads in the queue.

        This method continuously processes threads from the queue. It starts a new thread for each item in the queue,
        waits for the thread to finish, and marks the task as done.
        """
        while True:
            item = self.queue.get()
            if item is None:
                break
            target, args = item
            thread = threading.Thread(target=target, args=args)
            thread.start()
            thread.join()  # Wait for the thread to finish
            self.queue.task_done()

    def start(self):
        """
        Start the processing thread.

        This method starts the processing thread that handles the execution of threads from the queue. The processing
        thread runs in daemon mode and runs the `process_queue` method.
        """
        self.process_thread = threading.Thread(target=self.process_queue, daemon=True)
        self.process_thread.start()

    def stop(self):
        """
        Stop the processing thread.

        This method signals the processing thread to stop by adding a `None` item to the queue. It then waits for the
        processing thread to finish.
        """
        self.queue.put(None)  # Signal the processing thread to stop
        self.process_thread.join()  # Wait for the processing thread to finish


class DBHandler(logging.Handler):
    """
    Custom logging handler for database logging.

    This handler logs records to a database using SQLAlchemy.

    Methods:
        emit(record): Emit a log record to the database.
    """
    __conf: _LoggingConf
    __engine: Engine
    __session_class = None
    __base_path: str = os.path.dirname(sys.argv[0])
    __task_manager: DBTaskManager
    __last_ids: dict = {}

    def __init__(self):
        """
        Initialize a DBHandler instance.

        This constructor initializes a DBHandler instance for database logging. It sets up the configuration,
        database engine, session class, and task manager for processing log records. It also registers an exit handler
        to stop the task manager at program exit.

        """
        super().__init__()
        self.__conf = _LoggingConf()
        self.__engine = _LoggingConf().get_sa_engine()
        global logs_table
        if logs_table is None and self.__conf.logger_db_settings.table is not None:
            logs_table = self.__get_table(self.__conf.logger_db_settings.table, self.__conf.logger_db_settings.engine)
            # _metadata.create_all(self.__engine)
        self.__session_class = sessionmaker(bind=self.__engine)

        self.__task_manager = DBTaskManager()
        self.__task_manager.start()
        atexit.register(self.__exit_handler)

    def __exit_handler(self):
        """
        Handle program exit.

        This method is called at program exit to ensure that the task manager is stopped.

        """
        self.__task_manager.stop()

    @staticmethod
    def __get_table(name, engine):
        """
        Create a SQLAlchemy Table instance.

        Args:
            name (str): The name of the table.
            engine (str): The database engine.

        Returns:
            Table: A SQLAlchemy Table instance with columns defined for the given engine.

        """
        return Table(
            name,
            _metadata,
            *get_columns(engine)
        )

    def emit(self, record):
        """
        Emit a log record to the database.

        Args:
            record (logging.LogRecord): The log record to be emitted.
        """
        # Grab the __meta__. This should always be defined when sending a record.
        frame: LoggerFrame = record.__dict__["__meta__"]

        # Retrieve data from the frame.
        frame_dict = {col: val for col, val in frame._asdict().items() if col in logs_table.columns}
        if "file_name" in frame_dict.keys():
            frame_dict["file_name"] = frame_dict["file_name"].replace(self.__base_path, '')[1:]

        # Find any custom data and their columns with it.
        custom_data = {k: v for k, v in record.__dict__.get("custom_data", {}).items() if k in logs_table.columns}

        # Get additional data and record data.
        additional_data = {k: v for k, v in {
            "level": "EXCEPTION" if frame.is_exception else record.levelname,
            "message": record.getMessage(),
            "created_at": datetime.utcnow(),
            "main_script": sys.argv[0],
            "logger": record.name,
        }.items() if k in logs_table.columns}

        # Combine into one insert statement.
        log_entry = logs_table.insert().values(
            **additional_data,
            **frame_dict,
            **custom_data
        )

        # Queue the insert, so we don't lock the program waiting for the database to insert the record.
        # Because we calculate the datetime of the record to create above here, it will be sortable.
        if record.__dict__.get('last_inserted_id', None) is not None:
            self.__task_manager.stop()
            self.__last_ids[record.__dict__['last_inserted_id']] = self.__insert_record(log_entry)
            self.__task_manager.start()
        else:
            self.__task_manager.submit_thread(self.__insert_record, (log_entry,))

    def __insert_record(self, record):
        """
        Insert a log record into the database.

        Args:
            record: The SQLAlchemy insert statement for the log record.

        This method is responsible for inserting a log record into the database. It opens a new database session,
        executes the provided insert statement, commits the transaction, and then closes the session.
        """
        session = self.__session_class()
        result = session.execute(record)
        session.commit()
        inserted_ids = result.inserted_primary_key
        session.close()
        return inserted_ids

    @property
    def table(self):
        """
        Get or set the database table for logging.

        This property allows getting or setting the database table used for logging.

        Returns:
            Table: The current database table for logging.

        Setter:
            value (Table | sqlalchemy.orm.decl_api.DeclarativeMeta): The database table or SQLAlchemy declarative class
            to use for logging.
        """
        global logs_table
        return logs_table

    @table.setter
    def table(self, value: Union[Table, sqlalchemy.orm.decl_api.DeclarativeMeta]):
        """
        Set the database table for logging and create it.

        Args:
            value (Table | sqlalchemy.orm.decl_api.DeclarativeMeta): The database table or SQLAlchemy declarative class
            to use for logging.
        """
        global logs_table
        if isinstance(value, sqlalchemy.orm.decl_api.DeclarativeMeta):
            logs_table = value.__table__
        elif isinstance(value, Table):
            logs_table = value
        else:
            ...
        logs_table.metadata.create_all(self.__engine)

    def last_inserted_ids(self, last_inserted_identifier):
        last_ids = self.__last_ids.get(last_inserted_identifier, None)
        if last_ids is not None:
            del self.__last_ids[last_inserted_identifier]
        return last_ids
    """def __get_top_function(self):
        try:
            frame = inspect.currentframe().f_back.f_back.f_back.f_back.f_back.f_back.f_back
        except:
            frame = inspect.currentframe()
        top_frame = None
        trace = []

        # Traverse up the call stack to find the top frame
        while frame.f_back:
            top_frame = frame
            frame = frame.f_back
            trace.append(f"{top_frame.f_code.co_name}")

        if top_frame:
            return " -> ".join(trace)
        else:
            return None"""
