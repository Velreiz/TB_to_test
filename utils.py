import logging
from datetime import datetime

def setup_logger(name, log_file, level=logging.INFO):
    """Установка логгера для записи сообщений."""
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def log_message(logger, level, message):
   if logger is not None:
     logger.log(level, message)
   else:
     print(f'{datetime.now()} - {level} - {message}')