import datetime
from typing import Union
import os
from functools import lru_cache
import urllib.parse

import toml
from .models import LoggerDBSettings, ConsoleHandlerConf, FileHandlerConf
from ._static import merge_dicts

LOGGER_ENV_PREFIX = "_LOGGERBASE_"
DEFAULT_TEXT_FORMAT = '%(asctime)s [ %(levelname)-8s ] %(name)-40s=> %(message)s'

_DEFAULT_CONSOLE_HANDLER = ConsoleHandlerConf(level=20, text_format=DEFAULT_TEXT_FORMAT)


class _LoggingConf:
    """
    Configuration class for managing logging settings.

    This class provides methods to load and manage logging settings from environmental variables and configuration
    files. It also includes methods to create and configure SQLAlchemy engine.

    Attributes:
        console_config (ConsoleHandlerConf): Configuration for the console (stdout) handler.
        file_config (FileHandlerConf): Configuration for the file handler (if defined).

    Properties:
        logger_use (str): The chosen logger configuration (e.g., 'default').
        logger_conf_path (str): The path to the configuration file (if provided).
        logger_db_settings (LoggerDBSettings): Database settings for logging.
        log_level (int): The logging level to be used.

    Methods:
        load_env(): Load settings from environmental variables.
        __load_conf(): Load settings from the specified configuration file.
        get_sa_engine(): Create and return an SQLAlchemy engine.
        __get_sa_con_string(): Generate an SQLAlchemy connection string.
    """
    __use: Union[str, None] = 'default'
    __level: int = 10
    __conf_path: Union[str, None]
    __db_settings: LoggerDBSettings
    console_config: ConsoleHandlerConf = _DEFAULT_CONSOLE_HANDLER
    file_config: FileHandlerConf = None

    def __init__(self):
        """
        Initialize the _LoggingConf class.

        Loads logging settings from environmental variables and configuration files.
        """
        self.load_env()
        if self.__conf_path is not None:
            if os.path.isfile(self.__conf_path):
                self.__load_conf()
            else:
                raise FileNotFoundError(f"Can not find config at {self.__conf_path}.")

    def load_env(self) -> None:
        """
        Load logging settings from environmental variables.

        Retrieves and updates logging settings from environmental variables.
        """
        self.__use = os.environ.get(f"{LOGGER_ENV_PREFIX}USE", self.__use)
        self.__conf_path = os.environ.get(f"{LOGGER_ENV_PREFIX}CONF")
        self.__db_settings = LoggerDBSettings(
            engine=os.environ.get(f"{LOGGER_ENV_PREFIX}DB_ENGINE"),
            database=os.environ.get(f"{LOGGER_ENV_PREFIX}DB_DATABASE"),
            host=os.environ.get(f"{LOGGER_ENV_PREFIX}DB_HOST"),
            port=os.environ.get(f"{LOGGER_ENV_PREFIX}DB_PORT"),
            username=os.environ.get(f"{LOGGER_ENV_PREFIX}DB_USERNAME"),
            password=os.environ.get(f"{LOGGER_ENV_PREFIX}DB_PASSWORD"),
            table=os.environ.get(f"{LOGGER_ENV_PREFIX}DB_TABLE")
        )

    def __load_conf(self):
        """
        Load logging settings from a configuration file.

        Loads and updates logging settings from a specified configuration file.
        """
        conf_data = self.__read_toml(self.__conf_path).get('logger', {})
        if self.__use is not None and self.__use in conf_data.keys():
            conf_data = merge_dicts(conf_data, conf_data.get(self.__use, {}).copy())
        elif 'use' in conf_data.keys():
            conf_data = merge_dicts(conf_data, conf_data.get(conf_data['use'], {}).copy())

        self.__level = conf_data.get('level', self.__level)
        self.console_config = ConsoleHandlerConf(
            level=conf_data.get('console_handler', {}).get('level', conf_data.get('level', 20)),
            text_format=conf_data.get('console_handler', {}).get('text_format', DEFAULT_TEXT_FORMAT)
        )

        fp = conf_data.get('file_handler', {}).get('file_path', None)
        if fp is not None:
            self.file_config = FileHandlerConf(
                level=conf_data.get('file_handler', {}).get('level', conf_data.get('level', 30)),
                text_format=conf_data.get('file_handler', {}).get('text_format', DEFAULT_TEXT_FORMAT),
                file_path=fp.format(DATETIME=datetime.datetime.now().strftime('%Y_%m_%d__%H_%M')),
                prefix=conf_data.get('file_handler', {}).get('prefix', '')
            )

    @lru_cache()
    def __read_toml(self, conf_path):
        if os.path.isfile(self.__conf_path):
            with open(conf_path, "r") as toml_file:
                return toml.load(toml_file)
        else:
            print(FileNotFoundError(f"Can not find config at {self.__conf_path}."))

    # We create the SA engine in this class to protect the password from leaking.
    def get_sa_engine(self):
        """
        Create and return an SQLAlchemy engine.

        Returns:
            Engine: The SQLAlchemy engine for logging.
        """
        if self.__db_settings.engine is None or self.__db_settings.table is None:
            return None
        try:
            from sqlalchemy import create_engine
        except ImportError:
            raise ImportError(f"Install sqlalchemy to use the {LOGGER_ENV_PREFIX}DB environment variables")
        return create_engine(self.__get_sa_con_string())

    def __get_sa_con_string(self):
        """
        Generate an SQLAlchemy connection string.

        Generates an SQLAlchemy connection string based on the defined database settings.

        Returns:
            str: The SQLAlchemy connection string.
        """
        con = self.__db_settings.engine + "://"
        con += urllib.parse.quote(self.__db_settings.username) if self.__db_settings.username is not None else ""
        if self.__db_settings.password is not None and self.__db_settings.password:
            con += f":{urllib.parse.quote(self.__db_settings.password)}"
        if self.__db_settings.host is not None and self.__db_settings.host:
            con += f"@{self.__db_settings.host}"
        if self.__db_settings.port is not None and self.__db_settings.port:
            con += f":{self.__db_settings.port}"
        if self.__db_settings != "sqlite":
            con += "/"
        if self.__db_settings.database is not None and self.__db_settings.database:
            con += self.__db_settings.database
        return con

    @property
    def logger_use(self):
        """
        Get the chosen logger configuration.

        Returns:
            str: The selected logger configuration (e.g., 'default').
        """
        return self.__use

    @property
    def logger_conf_path(self):
        """
        Get the path to the configuration file.

        Returns:
            str: The path to the configuration file (if provided).
        """
        return self.__conf_path

    @property
    def logger_db_settings(self):
        """
        Get the database settings for logging.

        Returns:
            LoggerDBSettings: Database settings for logging.
        """
        return LoggerDBSettings(
            engine=self.__db_settings.engine,
            database=self.__db_settings.database,
            host=self.__db_settings.host,
            port=self.__db_settings.port,
            table=self.__db_settings.table,
            username=self.__db_settings.username,
            password="***"
        )

    @property
    def log_level(self):
        """
        Get the logging level to be used.

        Returns:
            int: The logging level (e.g., 10 for DEBUG, 20 for INFO).
        """
        return self.__level
