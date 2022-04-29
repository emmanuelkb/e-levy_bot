import logging
from pythonjsonlogger import jsonlogger


def setup_custom_logger(log_level):
    logger = logging.getLogger(__name__)

    if not len(logger.handlers):
        logger.setLevel(log_level)
        json_handler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter(
            fmt='%(message)s %(body)s %(levelname)s %(asctime)s %(filename)s %(module)s %(funcName)s %(lineno)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
        json_handler.setFormatter(formatter)
        logger.addHandler(json_handler)
        logger.propagate = False
    return logger
