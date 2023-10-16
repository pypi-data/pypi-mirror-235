import sys
import logging

logging.basicConfig(level=logging.INFO)


class Logger:
    name: str | None
    level: int | None
    logger: logging.Logger | None

    def __new__(cls, name: str, level: int, *args, **kwargs):
        if name is None:
            raise KeyError(
                "Logger name cannot be None"
            )
        if level is None:
            level = logging.INFO
        object_ = super().__new__(cls, name, level)
        return object_

    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg)


# GitHub actions and tests
def git_path_loader():
    sys.path.append(__file__.rstrip("main.py"))


if sys.argv.count("-git") > 0:
    git_path_loader()
