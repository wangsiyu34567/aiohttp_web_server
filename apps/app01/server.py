import logging

from aiohttp import web

from apps.app01.urls import sub_app
from apps.app01.middlewares import get_middlewares
from core.server.server_run import go
from core.logging.base_log import get_logger
from configs .bases import LOG_CONFIG


logging.basicConfig(level=LOG_CONFIG['console']['level'],
                    format=LOG_CONFIG['console']['formatter'])


async def web_server(loop, sock):
    middlewares = get_middlewares()
    app = web.Application(loop=loop, middlewares=middlewares, logger=get_logger(__name__))
    app.add_subapp('/api', sub_app)
    handler = await loop.create_server(app.make_handler(), sock=sock, backlog=100)  # 测试backlog可适当调低
    return handler


def run(sock):
    go(sock, web_server)
