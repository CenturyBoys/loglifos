import concurrent.futures
import datetime
import inspect
import json
import logging
import traceback
from enum import IntEnum

# Set always the root level to ERROR on init
_root_logger = logging.getLogger("root")
_root_logger.setLevel(logging.ERROR)

# Initialize loglifos with default values StreamHandler with JSON formatter and ERROR log level.
_loglifos = logging.getLogger("loglifos")
_loglifos.setLevel(logging.ERROR)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(message)s")
ch.setFormatter(formatter)
_loglifos.addHandler(ch)

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


class LogType(IntEnum):
    JSON = 0
    TEXT = 1


log_type = LogType.JSON


class SingleExecutor:
    __executor = None

    @classmethod
    def get_executor(cls):
        if cls.__executor is None:
            cls.__executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        return cls.__executor


def __format_message(
    msg, level: str, *args, exception: Exception = None, **kwargs
) -> str:
    stack = inspect.stack()[2]
    _dict = {
        "time": str(datetime.datetime.utcnow()),
        "level": level,
        "file": str(stack.filename),
        "function": str(stack.function),
        "msg": msg,
    }
    for attr, value in kwargs.items():
        if hasattr(value, "__repr__"):
            value = repr(value)
        _dict.update({attr: value})
    if args:
        _dict.update({"args": repr(args)})
    if exception:
        _dict.update({"error": "".join(traceback.format_exception(exception))})
    if log_type == LogType.JSON:
        message = json.dumps(_dict)
    else:
        list_message = [f"{key.title()}: {value}" for key, value in _dict.items()]
        list_message.insert(0, "#" * 50)
        message = "\n".join(list_message)
    return message


def debug(msg, *args, **kwargs):
    json_repr = __format_message(msg, "DEBUG", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(_loglifos.debug, json_repr)


def info(msg, *args, **kwargs):
    json_repr = __format_message(msg, "INFO", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(_loglifos.info, json_repr)


def warning(msg, *args, **kwargs):
    json_repr = __format_message(msg, "WARNING", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(_loglifos.warning, json_repr)


def error(msg, *args, exception: Exception = None, **kwargs):
    json_repr = __format_message(msg, "ERROR", exception=exception, *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(_loglifos.error, json_repr)


def critical(msg, *args, **kwargs):
    json_repr = __format_message(msg, "CRITICAL", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(_loglifos.critical, json_repr)


def set_config(log_level: int = ERROR):
    _loglifos.setLevel(log_level)


def set_log_type(new_type: LogType = LogType.JSON):
    global log_type  # pylint: disable=W0603
    log_type = new_type
