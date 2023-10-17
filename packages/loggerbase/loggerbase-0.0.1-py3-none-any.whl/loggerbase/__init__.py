"""
loggerbase: Logging Utilities
-------------------------

This package provides a set of logging utilities to simplify and streamline the logging process in your Python
applications.

Contents:
- LoggerBase: A customizable logger class for general logging purposes.
- StdLogger: Specialized loggers for standard output and standard error.
- ExceptionLogger: A logger for handling and logging exceptions.

Usage:
-------
1. Import the `logger` object from this package to access various loggers and exception handling.
2. Make YourClass inherit the LoggerBase class to access its functionality.

Example::

    from dotenv import load_dotenv

    from loggerbase import logger, LoggerBase

    load_dotenv(".env.example")  # Make the environment variables load. See the documentation on available variables
    logger.main.load_env()  # Reload the environment on all LoggerBase instances throughout the program.
    # logger.main.load_env(self_only=True)  # Only reload the environment for this logger.

    logger.stdout.start_capture()       # Capture all stdout and output it with your logger settings.
    logger.stderr.start_capture()       # Capture all stderr and output it with your logger settings.
    logger.exceptions.start_capture()   # Capture exceptions and log them.

    logger.stdout.use_logger = logger.stderr.use_logger = True      # default on true
    logger.stdout.include_info = logger.stderr.include_info = True  # default false, Does nothing when use_logger = True

    logger.main.info("Hello")  # Main Logger
    print("World")             # Will be captured by the stdout logger
    x = 0/0                    # Will be captured by the exception logger

"""
from .loggerbase import (
    LoggerBase,
)


class __StdLoggerHandler:
    """
    A class for managing logger instances.

    This class provides easy access to shared logger instances, such as the main logger,
    standard output (stdout) logger, standard error (stderr) logger, and exception logger.

    """
    # Import the StdLogger and ExceptionLogger classes
    from .loggerbase import StdLogger as __StdLogger
    from .loggerbase import ExceptionLogger as __ExceptionLogger

    # Import the StdType enum
    from .enums import StdType as __StdType

    # Define class-level variables
    __type_std_type = __StdType
    __type_stdlogger = __StdLogger
    __type_exception_logger = __ExceptionLogger

    # Define shared logger instances
    __main_logger: LoggerBase = None
    __stdout_logger: __StdLogger = None
    __stderr_logger: __StdLogger = None
    __exception_logger: __ExceptionLogger = None

    @property
    def main(self):
        """
        Get the main logger instance.

        If the main logger instance exists, it is returned. Otherwise, a new
        LoggerBase instance named "main_logger" is created and returned.

        Returns:
            LoggerBase: The main logger instance.
        """
        if self.__main_logger is None:
            self.__main_logger = LoggerBase("main_logger")
        return self.__main_logger

    @property
    def stdout(self):
        """
        Get the standard output (stdout) logger instance.

        If the stdout logger instance exists, it is returned. Otherwise, a new
        StdLogger instance for stdout is created and returned.

        Returns:
            StdLogger: The stdout logger instance.
        """
        if self.__stdout_logger is None:
            self.__stdout_logger = self.__type_stdlogger(self.__type_std_type.STDOUT, LoggerBase("stdout_logger"))
        return self.__stdout_logger

    @property
    def stderr(self):
        """
        Get the standard error (stderr) logger instance.

        If the stderr logger instance exists, it is returned. Otherwise, a new
        StdLogger instance for stderr is created and returned.

        Returns:
            StdLogger: The stderr logger instance.
        """
        if self.__stderr_logger is None:
            self.__stderr_logger = self.__type_stdlogger(self.__type_std_type.STDERR, LoggerBase("stderr_logger"))
        return self.__stderr_logger

    @property
    def exceptions(self):
        """
        Get the exception logger instance.

        Returns:
            ExceptionLogger: The exception logger instance.
        """
        if self.__exception_logger is None:
            self.__exception_logger = self.__type_exception_logger(LoggerBase("exception_logger"))
        return self.__exception_logger


# Create an instance of the logger handler
logger = __StdLoggerHandler()
