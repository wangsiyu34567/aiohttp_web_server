import asyncio


def async_test(async_function):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(async_function)
        future = coro(*args, **kwargs)
        loop = asyncio.new_event_loop()
        loop.run_until_complete(future)
        loop.close()
    return wrapper


def run_test(modules):
    print(modules)
    pass