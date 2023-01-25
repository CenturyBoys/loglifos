# A logger python project
```
 ,-----------------------------------------------------------------v
 u           ,-~~\   <~)_   u\             /\    ,-.       ,-.     u
 u  _,===-.,  (   \   ( v~\ u u  _,===-.,  \/   <,- \_____/  `     u
 u (______,.   u\. \   \_/'  \u (______,. /__\    /  ___. \  -===- u
 u            _a_a`\\  /\     u           \--/ ,_(__/ ,_(__\       u
 `--------------------------------------------- By CenturyBoys ----y
```

This is a non block JSON logger that use python's default logger with a thread executor.

By default loglifos set the default root loger to ERROR level

### Settings

You can change loglifos log level using ```set_config``` method. Loglifos use the same level constants as the default logging python lib. 

 ```python
import loglifos

loglifos.set_config(loglifos.ERROR)
```

### Using

```python
import loglifos

try:
    a = 1 / 0 
except Exception as e:
    loglifos.debug("Message from debug", "some args", 1, some__kwargs="Kwargs of debug")
    loglifos.info("Message from info", "some args", 1, some__kwargs="Kwargs of info")
    loglifos.warning("Message from warning", "some args", 1, some__kwargs="Kwargs of warning")
    loglifos.error("Message from error", "some args", 1, some__kwargs="Kwargs of error", exception=e)
    loglifos.critical("Message from critical", "some args", 1, some__kwargs="Kwargs of critical")
```
```bash
{"time": "2023-01-25 13:27:34.896765", "level": "ERROR", "file": "/home/marco/.config/JetBrains/PyCharmCE2022.3/scratche
  s/scratch_1.py", "function": "<module>", "msg": "Message from error", "some__kwargs": "'Kwargs of error'", "args": "('
  some args', 1)", "error": "Traceback (most recent call last):\n  File \"/home/marco/.config/JetBrains/PyCharmCE2022.3/
  scratches/scratch_1.py\", line 9, in <module>\n    a = 1 / 0\nZeroDivisionError: division by zero\n"}
{"time": "2023-01-25 13:27:34.899420", "level": "DEBUG", "file": "/home/marco/.config/JetBrains/PyCharmCE2022.3/scratche
  s/scratch_1.py", "function": "<module>", "msg": "Message from debug", "some__kwargs": "'Kwargs of debug'", "args": "('
  some args', 1)"}
{"time": "2023-01-25 13:27:34.899676", "level": "INFO", "file": "/home/marco/.config/JetBrains/PyCharmCE2022.3/scratches
  /scratch_1.py", "function": "<module>", "msg": "Message from info", "some__kwargs": "'Kwargs of info'", "args": "('som
  e args', 1)"}
{"time": "2023-01-25 13:27:34.899885", "level": "WARNING", "file": "/home/marco/.config/JetBrains/PyCharmCE2022.3/scratc
  hes/scratch_1.py", "function": "<module>", "msg": "Message from warning", "some__kwargs": "'Kwargs of warning'", "args
  ": "('some args', 1)"}
{"time": "2023-01-25 13:27:34.900066", "level": "CRITICAL", "file": "/home/marco/.config/JetBrains/PyCharmCE2022.3/scrat
  ches/scratch_1.py", "function": "<module>", "msg": "Message from critical", "some__kwargs": "'Kwargs of critical'", "a
  rgs": "('some args', 1)"}
```
