from aiohttp import web


class Index(web.View):

    async def get(self):

        return web.json_response(text='hello word')
