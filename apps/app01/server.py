import sys
import logging

from aiohttp import web

from apps.app01.urls import sub_app
from apps.app01.middlewares import get_middlewares
from core.server.server_run import go
from core.logging.base_log import get_logger


logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


async def web_server(loop, sock):
    middlewares = get_middlewares()
    app = web.Application(middlewares=middlewares, logger=get_logger(__name__))
    app.add_subapp('/api', sub_app)
    handler = await loop.create_server(app.make_handler(), sock=sock)
    return handler


def run(sock):
    go(sock, web_server)
