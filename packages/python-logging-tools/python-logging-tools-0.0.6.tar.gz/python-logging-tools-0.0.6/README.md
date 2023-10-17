![PyPI - Version](https://img.shields.io/pypi/v/python-logging-tools)
![GitHub Workflow Status (with event)](https://github.com/MGS-Daniil/python-logging-tools/actions/workflows/python-app.yml/badge.svg)
# python logging tools
python package for logging

# installation
```commandline
pip install python-logging-tools
```

## usage:
```python
import python_logging_tools

log = python_logging_tools.LoggingTools("Name", logging.INFO)
log.debug("message")
```
output:
[INFO]> [Name] - message```

## package:
- [x] this package simplifies logging in python
logging tools package
- [x] logging levels are supported
- [ ] colors are supported
