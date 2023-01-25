import unittest.mock
from logging import Logger

from freezegun import freeze_time

import loglifos


def test_set_config():
    loglifos.set_config(loglifos.ERROR)


@freeze_time("2023-01-01T10:10:10.000000")
def test_debug():
    with unittest.mock.patch.object(Logger, "debug") as mock_call:
        future = loglifos.debug("message", 123, meu_loro="debug")
    future.result()
    assert mock_call.call_args.args == (
        '{"time": "2023-01-01 10:10:10", "level": "DEBUG", "file": "/home/marco/projects/loglifos/tests/te'
        'st_logs.py", "function": "test_debug", "msg": "message", "meu_loro": "\'debug\'", "args": "(123,)'
        '"}',
    )


@freeze_time("2023-01-01T10:10:10.000000")
def test_info():
    with unittest.mock.patch.object(Logger, "info") as mock_call:
        future = loglifos.info("message", 123, meu_loro="debug")
    future.result()
    assert mock_call.call_args.args == (
        '{"time": "2023-01-01 10:10:10", "level": "INFO", "file": "/home/marco/projects/loglifos/tests/te'
        'st_logs.py", "function": "test_info", "msg": "message", "meu_loro": "\'debug\'", "args": "(123,)'
        '"}',
    )


@freeze_time("2023-01-01T10:10:10.000000")
def test_warning():
    with unittest.mock.patch.object(Logger, "warning") as mock_call:
        future = loglifos.warning("message", 123, meu_loro="debug")
    future.result()
    assert mock_call.call_args.args == (
        '{"time": "2023-01-01 10:10:10", "level": "WARNING", "file": "/home/marco/projects/loglifos/tests'
        '/test_logs.py", "function": "test_warning", "msg": "message", "meu_loro": "\'debug\'", "args": "'
        '(123,)"}',
    )


@freeze_time("2023-01-01T10:10:10.000000")
def test_critical():
    with unittest.mock.patch.object(Logger, "critical") as mock_call:
        future = loglifos.critical("message", 123, meu_loro="debug")
    future.result()
    assert mock_call.call_args.args == (
        '{"time": "2023-01-01 10:10:10", "level": "CRITICAL", "file": "/home/marco/projects/loglifos/tes'
        'ts/test_logs.py", "function": "test_critical", "msg": "message", "meu_loro": "\'debug\'", "args'
        '": "(123,)"}',
    )


@freeze_time("2023-01-01T10:10:10.000000")
def test_error():
    with unittest.mock.patch.object(Logger, "error") as mock_call:
        try:
            raise Exception("meu lorito")
        except Exception as error:
            future = loglifos.error("message", 123, exception=error, meu_loro="debug")
    future.result()
    assert mock_call.call_args.args == (
        '{"time": "2023-01-01 10:10:10", "level": "ERROR", "file": "/home/marco/projects/loglifos/tests/t'
        'est_logs.py", "function": "test_error", "msg": "message", "meu_loro": "\'debug\'", "args": "(123'
        ',)", "error": "Traceback (most recent call last):\\n  File \\"/home/marco/projects/loglifos/test'
        's/test_logs.py\\", line 65, in test_error\\n    raise Exception(\\"meu lorito\\")\\nException: m'
        'eu lorito\\n"}',
    )
