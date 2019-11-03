from aiohttp import web
from .views.index import Index

sub_app = web.Application()

sub_app.router.add_view('/index', Index, name='index')
