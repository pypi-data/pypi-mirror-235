import os
import sys

from dotenv import load_dotenv  # pip install python-dotenv
import pytest

from loggerbase.conf import _LoggingConf as LoggingConf


def test_base_conf():
    conf = LoggingConf()
    assert isinstance(conf, LoggingConf)


def test_run_example_one():
    from loggerbase import logger

    load_dotenv(f"{os.path.dirname(__file__)}/../examples/basic/.env.example")
    os.environ["_LOGGERBASE_CONF"] = f"{os.path.dirname(__file__)}/../examples/basic/logger_conf.toml"

    logger.main.load_env()

    logger.main.debug("Hello from debug")
    logger.main.info("Hello from info")
    logger.main.warning("Hello from warning")
    logger.main.error("Hello from error")
    logger.main.critical("Hello from critical")

    del logger
    os.remove("debug_log")


def test_run_example_two():
    from loggerbase import logger

    load_dotenv(f"{os.path.dirname(__file__)}/../examples/basic/.env.example")
    os.environ["_LOGGERBASE_CONF"] = f"{os.path.dirname(__file__)}/../examples/basic/logger_conf.toml"

    logger.main.load_env()

    logger.stdout.start_capture()
    logger.stderr.start_capture()
    logger.exceptions.start_capture()

    print("This is stdout")  # [ INFO     ] stdout_logger                 => This is stdout
    sys.stderr.write("This is on stderr")  # [ ERROR    ] stderr_logger                 => This is on stderr

    logger.stdout.use_logger = logger.stderr.use_logger = False  # default on true, Will avoid using LoggerBase

    # The order might seem off, so it's best to just use one of the 2.
    print("This is stdout 2")  # __main__.<module>:28:: This is stdout 2
    sys.stderr.write("This is on stderr 2\n")  # __main__.<module>:29:: This is on stderr 2

    # Exceptions are also handled. Will generate a ZeroDivisionError exception.
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0

    del logger
