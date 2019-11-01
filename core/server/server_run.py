import os
import asyncio


def go(sock, web_server):
    try:
        import uvloop
        loop = uvloop.new_event_loop()
    except:
        loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)
    loop.run_until_complete(web_server(loop, sock))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
        print('stop server pid:', os.getpid())
