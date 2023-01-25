import concurrent.futures
import datetime
import inspect
import json
import logging
import traceback


# Set always the root level to ERROR on init
root_logger = logging.getLogger("root")
root_logger.setLevel(logging.ERROR)

# Initialize loglifos with default values StreamHandler with JSON formatter and ERROR log level.
loglifos = logging.getLogger("loglifos")
loglifos.setLevel(logging.ERROR)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(message)s")
ch.setFormatter(formatter)
loglifos.addHandler(ch)


class SingleExecutor:
    __executor = None

    @classmethod
    def get_executor(cls):
        if cls.__executor is None:
            cls.__executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        return cls.__executor


def __to_json(msg, level: str, *args, exception: Exception = None, **kwargs) -> str:
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
    return json.dumps(_dict)


def debug(msg, *args, **kwargs):
    json_repr = __to_json(msg, "DEBUG", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(loglifos.debug, json_repr)


def info(msg, *args, **kwargs):
    json_repr = __to_json(msg, "INFO", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(loglifos.info, json_repr)


def warning(msg, *args, **kwargs):
    json_repr = __to_json(msg, "WARNING", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(loglifos.warning, json_repr)


def error(msg, *args, exception: Exception = None, **kwargs):
    json_repr = __to_json(msg, "ERROR", exception=exception, *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(loglifos.error, json_repr)


def critical(msg, *args, **kwargs):
    json_repr = __to_json(msg, "CRITICAL", *args, **kwargs)
    executor = SingleExecutor.get_executor()
    return executor.submit(loglifos.critical, json_repr)


def set_config(log_level: int = logging.ERROR):
    loglifos.setLevel(log_level)
