from .middlewares import auth_middlerware, gloab_logger


async def base_middlewares(base=''):
    middlewares = []
    if not base or not isinstance(base, (dict,)):
        return middlewares

    if base.get('log'):
        middlewares.append(gloab_logger)

    if base.get('auth'):
        middlewares.append(auth_middlerware)

    return middlewares
