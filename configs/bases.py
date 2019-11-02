import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODULES = [
    'apps',
    'core',
    'tests',
]

MIDDLEWARES = {'log': True, 'auth': True}

WHITELIST = []

SERVICE_TYPE = 'SERVICE_TYPE'

LOG_CONFIG = {
    'type': ['file', 'console'],
    'file': {'formatter': '%(asctime)s -- %(name)s -- %(lineno)s -- %(levelname)s -- %(message)s',
             'dir_path': './log',
             'level': 20},
    'console': {'formatter': '%(asctime)s -- %(name)s -- %(lineno)s -- %(levelname)s -- %(message)s',
                'level': 20},
    'log_type': ['application/json', ]
}
