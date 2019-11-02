import os
import logging
from configs import bases
from configs.bases import LOG_CONFIG
from .log_handler import MyLoggerHandler


def file_log_format():
    dir_path = os.path.join(LOG_CONFIG['file'].get('dir_path', './'), bases.SERVICE_TYPE)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    filename = os.path.join(dir_path, '{}.log'.format(bases.SERVICE_TYPE))
    fh = MyLoggerHandler(filename, when="D", backupCount=30)
    if LOG_CONFIG['file'].get('formatter'):
        formatter_str = LOG_CONFIG['file']['formatter']
    else:
        formatter_str = '%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s'
    formatter = logging.Formatter(formatter_str)
    fh.setFormatter(formatter)

    level = LOG_CONFIG['file'].get('level', logging.DEBUG)
    fh.setLevel(level)
    return fh


def console_log_format():
    ch = logging.StreamHandler()
    if LOG_CONFIG['console'].get('formatter'):
        formatter_str = LOG_CONFIG['file']['formatter']
    else:
        formatter_str = '%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s'

    formatter = logging.Formatter(formatter_str)
    ch.setFormatter(formatter)
    level = LOG_CONFIG['console'].get('level', logging.INFO)
    ch.setLevel(level)
    return ch


def get_logger(name):
    logger = logging.getLogger(name)

    if 'file' in LOG_CONFIG['type']:
        logger.addHandler(file_log_format())

    return logger
