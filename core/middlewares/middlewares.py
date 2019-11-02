import sys
import re
from aiohttp.web import json_response, middleware, HTTPException, Response
from configs.bases import LOG_CONFIG, WHITELIST
from core.logging.base_log import get_logger

logger = get_logger(__name__)


@middleware
async def gloab_logger(request, handler):
    async def request_logger():
        try:
            if request.headers.get('Content-Type') in LOG_CONFIG['log_type']:
                body = await request.read()
            else:
                body = request.headers

            log_msg = 'request -- {ip} -- {rel_url} -- {body}'.format(
                **{'ip': request.headers.get('X-Forwarded-For'),
                   'rel_url': request.rel_url,
                   'body': body})
            logger.debug(log_msg)
        except Exception as e:
            logger.error(e)

    async def response_logger(response):
        try:
            if request.headers.get('Content-Type') in LOG_CONFIG['log_type']:
                body = response.body
            else:
                body = response.headers
            log_msg = 'response -- {body}'.format(**{'body': body})
            logger.debug(log_msg)
        except Exception as e:
            logger.error(e)

    async def middleware_handler():
        try:
            resp = await handler(request)
        except HTTPException as e:
            await request_logger()
            await response_logger(e)
            if e.status >= 500:
                return Response(text='<h1 style="text-align: center;">{}</h1>'.format(e.text),
                                status=e.status,
                                content_type='text/html')
            if e.status >= 400:
                return Response(text='<h1 style="text-align: center;">{}</h1>'.format(e.text),
                                status=e.status,
                                content_type='text/html')

            return json_response(data={'result': [], 'msg': 'maybe server is error?'}, status=e.status)
        log_msg = '{method} -- {rel_url} -- {status} -- {length}'
        logger.info(log_msg.format(**{'method': request.method,
                                      'rel_url': request.rel_url,
                                      'status': resp.status,
                                      'length': sys.getsizeof(resp.body)}))

        return resp

    return await middleware_handler()


@middleware
async def auth_middlerware(request, handler):
    async def middleware_handler():
        if any([re.match(white_url, request.path) for white_url in WHITELIST]):
            setattr(request, 'user', {})
        else:
            pass
        resp = await handler(request)
        return resp

    return await middleware_handler()
