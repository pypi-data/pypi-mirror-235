import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from textual.logging import TextualHandler

from re_renamer import PATH_LOG_FP, REGEX_LOG_FP


def create_rotating_log(
    name: str, fp: Path, level: int = logging.INFO
) -> logging.Logger:
    """Create a rotating file handler, that is also attached to the Textual logger.

    Args:
        name: Logger name.
        fp: Path to log file.
        level: Log level for handler. Defaults to logging.INFO.

    Returns:
        Log handler.
    """
    if not fp.exists():
        create_file(fp)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger_file_handler = RotatingFileHandler(fp, maxBytes=1024)
    logger_file_handler.setLevel(level)
    logger_file_handler.setFormatter(logging.Formatter("%(asctime)s\t%(message)s"))
    logger.addHandler(TextualHandler())
    logger.addHandler(logger_file_handler)
    return logger


def create_file(fp: Path) -> None:
    """Create a file and it's parents if needed.

    Args:
        fp: File path.
    """
    fp.parent.mkdir(parents=True, exist_ok=True)
    if not fp.exists():
        fp.touch()


# setup a logger for rename history
path_logger = create_rotating_log("re-namer", PATH_LOG_FP)

# setup a logger for regex history
regex_logger = create_rotating_log("regex", REGEX_LOG_FP)
