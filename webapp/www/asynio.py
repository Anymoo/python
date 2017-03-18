import asyncio

@asyncio.coroutine
def hello():
    print("hello world")
    r=yield from asyncio.sleep(10)        #异步调用asynio.sleep（）
    print("hello again")

loop=asyncio.get_event_loop()            #获取eventloop
loop.run_until_complete(hello())         #执行coroutine

