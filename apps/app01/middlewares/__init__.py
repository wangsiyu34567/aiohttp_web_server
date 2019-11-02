from core.middlewares import base_middlewares
from configs.bases import MIDDLEWARES


def get_middlewares():
    middlewares = base_middlewares(MIDDLEWARES)

    return middlewares
