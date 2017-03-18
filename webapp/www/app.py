import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html',charset='UTF-8')
@asyncio.coroutine         #把一个generator标记为coroutine（协程）类型，然后丢到eventloop里
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9900)
    logging.info('server started at http://127.0.0.1:9900')
    return srv
loop = asyncio.get_event_loop()        #获取eventloop
loop.run_until_complete(init(loop))    #执行coroutine
loop.run_forever()

