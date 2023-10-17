import logging
import os
import sys
import traceback
from typing import Union

from .conf import _LoggingConf
from .enums import StdType
from .models import LoggerFrame
from ._static import calculate_frame, merge_dicts
try:
    from .database import DBHandler
except ImportError:
    DBHandler = None

_exception_handled = False


class _LoggerMeta(type):
    """
    Metaclass for LoggerBase, StdLogger, and ExceptionLogger classes.

    This metaclass is responsible for handling various tasks related to logging configuration and behavior.
    It is used to control the behavior of specific methods in the LoggerBase, StdLogger, and ExceptionLogger classes.

    Attributes:


    Methods:
        register_instance(std_type, instance):
            Register an instance of a StdLogger for either standard output (STDOUT) or standard error (STDERR).

        register_logger(name, logger):
            Register a logger instance with a specific name.

        std_err_logger:
            Property that provides access to the standard error logger instance.

        std_out_logger:
            Property that provides access to the standard output logger instance.

        wrap_function(method):
            A decorator method that wraps functions to control the behavior of standard logging methods.

    :Note:
        This metaclass is used to disable standard logging methods for specific classes and functions defined in
        the __disable_std_log_for list. It also registers logger instances and standard loggers.

    """
    __disable_std_log_for = [
        # (Class, Function), Only works for classes which hold this metaclass under its self.__class__
        ("LoggerBase", "debug"),
        ("LoggerBase", "info"),
        ("LoggerBase", "warning"),
        ("LoggerBase", "error"),
        ("LoggerBase", "critical"),
        ("LoggerBase", "__init__"),
        ("ExceptionLogger", "__detect_exception"),
    ]
    _std_err_logger: 'StdLogger' = None
    _std_out_logger: 'StdLogger' = None
    _active_loggers = {}

    # def __init__(cls, name, bases, attrs):
    #    super(_LoggerMeta, cls).__init__(name, bases, attrs)  # Call the metaclass' __init__ method

    def __new__(cls, name, bases, attrs):
        """
        Customize and modify class attributes during class creation.

        This special method is invoked when creating a new class instance. In the context of the `_LoggerMeta`
        metaclass, it is used to customize and modify the attributes of a class being created.

        Parameters:
            cls (Type[Self]): The metaclass itself.
            name (str): The name of the class being created.
            bases (tuple): The base classes of the new class.
            attrs (dict): The attributes and methods of the new class.

        Returns:
            type: The new class instance with potential modifications to its attributes and methods.

        Usage:
            This method is employed to customize the behavior of the new class, especially in cases where specific
            methods within that class need to be modified. In the `_LoggerMeta` metaclass, it identifies methods that
            should have standard logging disabled and wraps them using the `wrap_function` decorator.
            It then returns the updated class instance.
        """
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and (name, attr_name) in cls.__disable_std_log_for:
                attrs[attr_name] = cls.wrap_function(attr_value)
        new_class = super().__new__(cls, name, bases, attrs)
        return new_class

    @classmethod
    def register_instance(cls, std_type: StdType, instance: 'StdLogger'):
        """
        Register an instance of the StdLogger for a specific standard output type.

        This class method allows registering an instance of the `StdLogger` class for either standard output (`stdout`)
        or standard error output (`stderr`). Once registered, these instances can be used to control and capture
        log messages for the specified output type.

        Parameters:
            cls (type): The metaclass itself.
            std_type (StdType): The type of standard output to register the instance for
                                (StdType.STDOUT or StdType.STDERR).
            instance (StdLogger): The instance of the StdLogger class to register.

        Usage:
            This method is used to register instances of the StdLogger class for controlling and capturing log messages.
            By specifying the `std_type`, you can register an instance for either standard output or
            standard error output. This enables the management of log messages for these output types.
        """
        if std_type == StdType.STDOUT:
            cls._std_out_logger = instance
        elif std_type == StdType.STDERR:
            cls._std_err_logger = instance

    @classmethod
    def register_logger(cls, name: str, logger: 'LoggerBase'):
        """
        Register a logger instance with a specified name.

        This class method allows registering instances of the `LoggerBase` class with a unique name. Registered logger
        instances can be referenced and managed later by their assigned names.

        Parameters:
            cls (Type[Self]): The metaclass itself.
            name (str): The unique name to identify the logger instance.
            logger (LoggerBase): The logger instance to register.

        Usage:
            This method is used to register logger instances with unique names, making it easier to reference and manage
            multiple loggers across the application.
        """
        cls._active_loggers[name] = logger

    @property
    def std_err_logger(self):
        """
        Property for accessing the standard error (stderr) logger instance.

        This property allows access to the `StdLogger` instance responsible for capturing and controlling log messages
        written to the standard error output (stderr). The `StdLogger` instance associated with standard error can be
        used to manage and capture log messages written to stderr.

        Returns:
            StdLogger: The instance of the StdLogger for standard error (stderr).

        Usage:
            Use this property to access the StdLogger instance responsible for managing log messages written to standard
            error (stderr).

        Example:
            std_err_logger = SomeClass.std_err_logger
            std_err_logger.start_capture()  # Begin capturing stderr log messages.
        """
        return self._std_err_logger

    @property
    def std_out_logger(self):
        """
        Property for accessing the standard output (stdout) logger instance.

        This property allows access to the `StdLogger` instance responsible for capturing and controlling log messages
        written to the standard output (stdout). The `StdLogger` instance associated with standard output can be used to
        manage and capture log messages written to stdout.

        Returns:
            StdLogger: The instance of the StdLogger for standard output (stdout).

        Usage:
            Use this property to access the StdLogger instance responsible for managing log messages written to standard
            output (stdout).

        Example:
            std_out_logger = SomeClass.std_out_logger
            std_out_logger.start_capture()  # Begin capturing stdout log messages.
        """
        return self._std_out_logger

    @staticmethod
    def wrap_function(method):
        """
        Wrap a callable method to control standard output and error logging.

        This static method is used to wrap a callable method, typically a function or method within a class, with logic
        to temporarily control and capture standard output (stdout) and standard error (stderr) log messages. It does
        this by pausing the capturing of log messages, executing the original method, and then resuming log message
        capturing afterward.

        Parameters:
            method (callable): The method or function to wrap with log message control.

        Returns:
            callable: A wrapped version of the input method with log message control logic.

        Usage:
            Use this method to wrap other methods or functions to temporarily control and capture log messages. It is
            often used in the context of disabling standard logging for specific classes and functions.

        Example:
            def my_function():
                # Original function logic here
                print("This message will be captured by the logger.")

            wrapped_function = SomeClass.wrap_function(my_function)
            wrapped_function()  # Log messages will be captured by the logger.

        Note:
            The wrapped method can be used to control log messages by temporarily disabling the logger, which can be
            useful in scenarios where you want to capture and manage log messages for specific methods or functions.
        """
        def wrapper(self, *args, **kwargs):
            reactivate_std_err = False
            reactivate_std_out = False
            if self.__class__.std_err_logger and self.__class__.std_err_logger.is_logging:
                self.__class__.std_err_logger.stop_capture()
                reactivate_std_err = True
            if self.__class__.std_out_logger and self.__class__.std_out_logger.is_logging:
                self.__class__.std_out_logger.stop_capture()
                reactivate_std_out = True

            result = method(self, *args, **kwargs)

            if reactivate_std_err:
                self.__class__.std_err_logger.start_capture()
            if reactivate_std_out:
                self.__class__.std_out_logger.start_capture()

            return result
        return wrapper


class StdLogger(metaclass=_LoggerMeta):
    """
    Standard Logger for capturing STDOUT or STDERR streams.

    This class captures the standard output (STDOUT) or standard error (STDERR) streams and optionally logs the content.

    Attributes:
        stream: The standard stream (stdout or stderr) being captured.

    Methods:
        __init__(self, std_type: StdType, logger: 'LoggerBase', frame_index: int = 2):
            Initialize the StdLogger to capture STDOUT or STDERR and optionally log content.
        start_capture(self):
            Start capturing the standard stream and log the content.
        stop_capture(self):
            Stop capturing the standard stream and cease logging the content.
        write(self, text):
            Write captured content and optionally log it.
        flush(self):
            Flush the original standard stream.

        Properties:
        is_logging: Indicates whether logging of captured content is active.
        include_info: Controls whether source code information is included in log messages.
        use_logger: Controls whether log messages are logged by a logger.

    Note:
        The `StdLogger` class captures standard output (STDOUT) or standard error (STDERR) streams and can be configured
        to log the captured content. This can be useful for capturing and logging messages that are printed to these
        standard streams during program execution. You can control whether the captured content is logged and whether
        additional source code information is included in log messages.
    """
    __std_type: StdType
    __original_std = None
    __is_logging: bool = False
    __frame_index: int = 2
    __include_info: bool = False
    __use_logger: bool = True
    stream = None

    def __init__(self, std_type: StdType, logger: 'LoggerBase', frame_index: int = 2):
        """
        Initialize the StdLogger to capture STDOUT or STDERR and optionally log content.

        Parameters:
            std_type (StdType): The type of standard stream to capture (STDOUT or STDERR).
            logger (LoggerBase): The logger instance that will be used to log captured content.
            frame_index (int, optional): The frame index to use for capturing source code information. Default is 2.
        """
        self.__logger = logger
        sys.stderr.flush()
        self.__std_type = std_type
        self.__frame_index = frame_index
        self.__class__.register_instance(std_type, self)  # Register class within the metaclass

        if std_type == StdType.STDOUT:
            self.stream = self.__original_std = sys.stdout
        elif std_type == StdType.STDERR:
            self.stream = self.__original_std = sys.stderr
        else:
            # TODO: Custom Exception
            raise Exception("Wrong StdType. Please use STDERR or STDOUT")

    def start_capture(self):
        """
        Start capturing the standard stream and log the content.
        """
        if self.__std_type == StdType.STDOUT:
            sys.stdout = self
        elif self.__std_type == StdType.STDERR:
            sys.stderr = self
        self.__is_logging = True

    def stop_capture(self):
        """
        Stop capturing the standard stream and cease logging the content.
        """
        if self.__std_type == StdType.STDOUT:
            sys.stdout = self.__original_std
        elif self.__std_type == StdType.STDERR:
            sys.stderr = self.__original_std
        self.__is_logging = False

    def write(self, text):
        """
        Write captured content and optionally log it.

        Parameters:
            text (str): The text content to be written and logged.
        """
        # frame_info: LoggerFrame = calculate_frame(before=inspect.stack()[0].frame.f_code.co_qualname)
        # frame_info: LoggerFrame = calculate_frame(index=2)
        # index=2 is default and should be the frame before calling this.
        frame_info: LoggerFrame = calculate_frame(index=self.__frame_index)

        if not self.__use_logger:
            w = text
            if self.__include_info and text not in ['\n', '', ' ']:
                w = f"{frame_info.module}.{frame_info.function}" + ":" + str(frame_info.line_number) + ":: "
                w += text
            self.stream.write(w)  # => self.__logger handles this
        else:
            if text != '\n':
                if self.__std_type == StdType.STDOUT:
                    self.__logger.info(text, extra={"__meta__": frame_info})
                elif self.__std_type == StdType.STDERR:
                    self.__logger.error(text)
            else:
                self.stream.write(text)
        self.flush()

    def flush(self):
        """
        Flush the original standard stream.
        """
        self.__original_std.flush()

    @property
    def is_logging(self):
        """
        bool: Indicates whether logging of captured content is active.
        """
        return self.__is_logging

    @property
    def include_info(self) -> bool:
        """
        bool: Controls whether source code information is included in log messages.
        """
        return self.__include_info

    @include_info.setter
    def include_info(self, v: bool):
        """
        Setter for the include_info property.

        Parameters:
            v (bool): The new value for the include_info property.

        Raises:
            ValueError: If the input value is not a boolean.

        Note:
            This property controls whether source code information is included in log messages. Setting it to True
            includes source code information in log messages, while setting it to False excludes it.
        """
        if isinstance(v, bool):
            self.__include_info = v
        else:
            print(f"ERROR: StdLogger.include_info should be a boolean")

    @property
    def use_logger(self) -> bool:
        """
        bool: Controls whether log messages are logged by a logger.
        """
        return self.__use_logger

    @use_logger.setter
    def use_logger(self, value: bool):
        """
        Setter for the use_logger property.

        Parameters:
            value (bool): The new value for the use_logger property.

        Raises:
            ValueError: If the input value is not a boolean.

        Note:
            This property controls whether log messages are logged by a logger. Setting it to True logs messages,
            while setting it to False does not log them.
        """
        if isinstance(value, bool):
            self.__use_logger = value
            self.__include_info = not value
        else:
            print(f"ERROR: StdLogger.use_logger should be a boolean")


class ExceptionLogger(metaclass=_LoggerMeta):
    """
    Exception Logger for capturing and handling exceptions.

    This class captures unhandled exceptions, logs them, and prints the exception trace.

    Attributes:

    Methods:
        start_capture(self):
            Start capturing and handling unhandled exceptions.
        stop_capture() -> None:
            Stop capturing and handling unhandled exceptions.

    Note:
        The `ExceptionLogger` class is responsible for capturing and handling unhandled exceptions. It logs information
        about unhandled exceptions and prints the exception trace. This can be helpful for diagnosing and
        troubleshooting issues in a program.

    The `start_capture` method is used to enable exception capturing and handling, and the `stop_capture` method can be
    used to disable it.
    """
    __logger: 'LoggerBase'

    def __init__(self, logger: 'LoggerBase'):
        """
        Initialize the ExceptionLogger with a logger instance.

        Parameters:
            logger (LoggerBase): The logger instance used to log captured exception information.
        """
        self.__logger = logger

    def __detect_exception(self, exc_type, exc_value, exc_traceback):
        """
        Detect unhandled exceptions, log them, and print the exception trace.

        Parameters:
            exc_type: The type of the exception.
            exc_value: The exception instance.
            exc_traceback: The traceback information for the exception.
        """
        global _exception_handled
        if not _exception_handled:
            _exception_handled = True
            # try:
            trace = [[filename, lineno, funcname, code]
                     for filename, lineno, funcname, code in traceback.extract_tb(exc_traceback)]
            base_msg = f"{exc_value}"
            for filename, lineno, funcname, code in trace:
                msg = base_msg + f" => {code}"
                self.__logger.critical(msg, extra={
                    "__meta__": LoggerFrame(
                        module=exc_type.__name__,
                        file_name=filename,
                        line_number=lineno,
                        function=funcname,
                        frame_before=None,
                        is_exception=True
                    ),
                })
            # except:
            #     raise
            traceback.print_tb(exc_traceback)

    def start_capture(self):
        """
        Start capturing and handling unhandled exceptions.

        Note:
            This method enables the capturing and handling of unhandled exceptions. Once enabled, unhandled exceptions
            will be logged and their traces printed.
        """
        # Catch exceptions
        sys.excepthook = self.__detect_exception

    @staticmethod
    def stop_capture() -> None:
        """
        Stop capturing and handling unhandled exceptions.

        Note:
            This method disables the capturing and handling of unhandled exceptions. After calling this method,
            unhandled exceptions will not be captured, logged, or printed.
        """
        sys.excepthook = None


class LoggerBase(metaclass=_LoggerMeta):
    """
    Base Logger class for configuring and managing loggers.

    This class serves as the base for creating custom loggers. It provides methods for logging messages at different
    levels, such as debug, info, warning, error, and critical. Additionally, it allows the configuration of log file
    settings and database logging.

    :Private Attributes:
        __name (str): The name of the logger.
        __conf (_LoggingConf): Configuration settings for the logger.
        __logger (logging.Logger): The underlying logging instance.
        __file_handler (logging.FileHandler): The file handler for logging to a file.
        __console_handler (logging.StreamHandler): The console handler for logging to the console.
        __db_handler (DBHandler): The database handler for logging to a database (if configured).

    Attributes:

    :Private Methods:
        __create_file_handler(self):
            Create and configure the file handler for file-based logging.
        __create_console_handler(self):
            Create and configure the console handler for console-based logging.
        __get_extra():
            Get additional log record information based on the current call stack.
        __get_kwargs(self, old_kwargs):
            Merge additional log record information into the provided keyword arguments.

    Methods:
        __init__(self, name: str = None):
            Initialize the LoggerBase with an optional logger name.
        debug(self, msg: any, *args, **kwargs):
            Log a message with the debug level.
        info(self, msg: any, *args, **kwargs):
            Log a message with the info level.
        warning(self, msg: any, *args, **kwargs):
            Log a message with the warning level.
        error(self, msg: any, *args, **kwargs):
            Log an error message with the error level.
        critical(self, msg: any, *args, **kwargs):
            Log a critical message with the critical level.
        __activate_db(self):
            Activate database logging by adding a database handler to the logger.
        load_env(self, self_only: bool = False):
            Load environment settings and activate logging for the logger.
        __activate_siblings(cls):
            Activate logging for sibling loggers within the same class.

        Properties:
        db_active:
            A property indicating whether the database handler is active.
        logging_logger:
            A property providing access to the underlying logger instance.
        db_handler:
            A property providing access to the database handler (if configured).

    Note:
        The `LoggerBase` class serves as a foundational component for creating and configuring loggers.
        It can be extended to create custom loggers with specific logging behaviors and settings.
    """
    __name: str
    __conf: _LoggingConf
    __logger: logging.Logger
    __file_handler: logging.FileHandler
    __console_handler: logging.StreamHandler
    __db_handler: 'DBHandler' = None

    def __init__(self, name: str = None):
        """
        Initialize the LoggerBase with an optional logger name.

        Parameters:
            name (str, optional): The name of the logger. If not provided, a default name based on the module and
            class name is used.
        """
        if name is None:
            name = self.__name = f"{self.__module__}.{self.__class__.__name__}"
        self.__class__.register_logger(name, self)  # Register within the metaclass.
        self.__conf = _LoggingConf()                # Load up the config
        self.__logger = logging.getLogger(name)     # Create or get a logging instance.

        # If we already had the same class instance we already have a logger set up with this name.
        if len(self.__logger.handlers) > 0:
            # Check if we didn't have a DBHandler already
            self.load_env(self_only=True)
            self.debug(f"Instance {name} initialized.")
            return

        if self.__conf.log_level is not None:
            self.__logger.setLevel(self.__conf.log_level)

        # Create the file handler
        self.__create_file_handler()

        # Create the console handler
        self.__create_console_handler()

        # Load the environment and create the database handler
        self.load_env(self_only=True)

        self.debug(f"Instance {name} initialized.")

    def __create_file_handler(self):
        """
        Create and configure the file handler for file-based logging.
        """
        if self.__conf.file_config is not None:
            self.__file_handler = logging.FileHandler(
                self.__conf.file_config.prefix + self.__conf.file_config.file_path
            )
            self.__file_handler.setLevel(self.__conf.file_config.level)
            self.__file_handler.setFormatter(
                logging.Formatter(self.__conf.file_config.text_format)
            )
            self.__logger.addHandler(self.__file_handler)

    def __create_console_handler(self):
        """
        Create and configure the console handler for console-based logging.
        """
        self.__console_handler = logging.StreamHandler()
        self.__console_handler.setLevel(self.__conf.console_config.level)
        self.__console_handler.setFormatter(
            logging.Formatter(self.__conf.console_config.text_format)
        )
        self.__logger.addHandler(self.__console_handler)

    @staticmethod
    def __get_extra():
        """
        Get additional log record information based on the current call stack.
        """
        frame = calculate_frame(index=5)
        return {
            "__meta__": frame,
        }

    def __get_kwargs(self, old_kwargs):
        """
        Merge additional log record information into the provided keyword arguments.

        Parameters:
            old_kwargs (dict): The existing keyword arguments.

        Returns:
            dict: The updated keyword arguments.
        """
        new_kwargs = old_kwargs
        if 'extra' in old_kwargs:
            new_kwargs = {'extra': self.__get_extra()}
            new_kwargs = merge_dicts(new_kwargs, old_kwargs)
        else:
            new_kwargs['extra'] = self.__get_extra()
        return new_kwargs

    def debug(self, msg: any, return_id: bool = False, *args, **kwargs):
        """
        Log a message with the debug level.

        Parameters:
            msg (any): The message to be logged.
            return_id (bool) (optional): Returns the database table inserted id if true.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments to include in the log record.
        """
        ident = 0
        if return_id:
            ident = os.urandom(16)
            kwargs['extra']['last_inserted_id'] = ident
        new_kwargs = self.__get_kwargs(kwargs)
        self.__logger.debug(msg, *args, **new_kwargs)
        if return_id:
            return self.__db_handler.last_inserted_ids(ident)

    def info(self, msg: any, return_id: bool = False, *args, **kwargs):
        """
        Log a message with the info level.

        Parameters:
            msg (any): The message to be logged.
            return_id (bool) (optional): Returns the database table inserted id if true.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments to include in the log record.
        """
        ident = 0
        if return_id:
            ident = os.urandom(16)
            kwargs['extra']['last_inserted_id'] = ident
        new_kwargs = self.__get_kwargs(kwargs)
        self.__logger.info(msg, *args, **new_kwargs)
        if return_id:
            return self.__db_handler.last_inserted_ids(ident)

    def warning(self, msg: any, return_id: bool = False, *args, **kwargs):
        """
        Log a message with the warning level.

        Parameters:
            msg (any): The message to be logged.
            return_id (bool) (optional): Returns the database table inserted id if true.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments to include in the log record.
        """
        ident = 0
        if return_id:
            ident = os.urandom(16)
            kwargs['extra']['last_inserted_id'] = ident
        new_kwargs = self.__get_kwargs(kwargs)
        self.__logger.warning(msg, *args, **new_kwargs)
        if return_id:
            return self.__db_handler.last_inserted_ids(ident)

    def error(self, msg: any, return_id: bool = False, *args, **kwargs):
        """
        Log an error message with the error level.

        Parameters:
            msg (any): The error message to be logged.
            return_id (bool) (optional): Returns the database table inserted id if true.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments to include in the log record.
        """
        ident = 0
        if return_id:
            ident = os.urandom(16)
            kwargs['extra']['last_inserted_id'] = ident
        new_kwargs = self.__get_kwargs(kwargs)
        self.__logger.error(msg, *args, **new_kwargs)
        if return_id:
            return self.__db_handler.last_inserted_ids(ident)

    def critical(self, msg: any, return_id: bool = False, *args, **kwargs):
        """
        Log a critical message with the critical level.

        Parameters:
            msg (any): The critical message to be logged.
            return_id (bool) (optional): Returns the database table inserted id if true.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments to include in the log record.
        """
        ident = 0
        if return_id:
            ident = os.urandom(16)
            kwargs['extra']['last_inserted_id'] = ident
        new_kwargs = self.__get_kwargs(kwargs)
        self.__logger.critical(msg, *args, **new_kwargs)
        if return_id:
            return self.__db_handler.last_inserted_ids(ident)

    def __activate_db(self):
        """
        Activate database logging by adding a database handler to the logger.
        """
        # First delete the DBHandlers if we had any
        for h in self.__logger.handlers:
            if h.__class__.__qualname__ == 'DBHandler':
                self.__logger.handlers.remove(h)
                break

        # We can only create one if we get database variables.
        if self.__conf.get_sa_engine() is not None:
            from .database import DBHandler
            self.__db_handler = DBHandler()
            self.__logger.addHandler(self.__db_handler)

    def load_env(self, self_only: bool = False):
        """
        Load environment settings and activate logging for the logger.

        Parameters:
            self_only (bool, optional): If True, load environment settings for this logger only. If False, activate
            settings for sibling loggers within the same class.
        """
        self.__conf.load_env()
        self.__activate_db()
        if not self_only:
            self.__activate_siblings()

    @classmethod
    def __activate_siblings(cls):
        """
        Activate logging for sibling loggers within the same class.
        """
        for sibling_name, sibling in cls._active_loggers.items():
            sibling.load_env(self_only=True)

    @property
    def db_active(self):
        """
        A property indicating whether the database handler is active.
        """
        return self.__db_handler is not None

    @property
    def logging_logger(self):
        """
        A property providing access to the underlying logger instance.
        """
        return self.__logger

    @property
    def db_handler(self) -> Union['DBHandler', None]:
        """
        A property providing access to the database handler (if configured).

        Returns:
            Union[DBHandler, None]: The database handler instance or None if not configured.
        """
        return self.__db_handler
