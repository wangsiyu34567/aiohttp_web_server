import sys
import logging

from aiohttp import web

from core.server.server_run import go
from apps.app01.urls import sub_app

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


async def web_server(loop, sock):
    app = web.Application()
    app.add_subapp('/api', sub_app)
    handler = await loop.create_server(app.make_handler(), sock=sock)
    return handler


def run(sock):
    go(sock, web_server)
