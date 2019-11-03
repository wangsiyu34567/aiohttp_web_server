import sys
from aiohttp import web


class BaseView(web.View):

    async def serializer(self, data=None):
        """
        data: 传入的数据, 多个数据集是元素内容必须是list
        multi: 是否处理多个数据集合
        """
        serializer_class = self.serializer_class(self.request)
        _ = await serializer_class._init()
        func = getattr(serializer_class, sys._getframe().f_back.f_code.co_name)

        if data is None:
            result = await func()
        else:
            result = await func(data)
        return result
