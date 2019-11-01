import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODULES = [
    'apps',
    'core',
    'tests',
]

MIDDLEWARES = []

WHITELIST = []

SERVICE_TYPE = 'SERVICE_TYPE'