import asyncio,logging
#选择MySQL作为网站的后台数据库

#执行SQL语句进行操作，并将常用的SELECT、INSERT等语句进行函数封装

#在异步框架的基础上，采用aiomysql作为数据库的异步IO驱动

#将数据库中表的操作，映射成一个类的操作，也就是数据库表的一行映射成一个对象(ORM)

#整个ORM也是异步操作

#预备知识：Python协程和异步IO(yield from的使用)、SQL数据库操作、元类、面向对象知识、Python语法

# -*- -----  思路  ----- -*-
   # 如何定义一个user类，这个类和数据库中的表User构成映射关系，二者应该关联起来，user可以操作表User

    #通过Field类将user类的属性映射到User表的列中，其中每一列的字段又有自己的一些属性，包括数据类型，列名，主键和默认值


import aiomysql

#打印sql查询语句
def log(sql,args=()):
    logging.info('SQL:%s'%sql)

#创建一个全局地址池，每个http请求都从池中获得数据库连接
async def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    #全局变量__pool用于存储整个连接池
    global __pool
    __pool=await aiomysql.create_pool(
        #**kw参数包含所有连接需要用到的关键字参数
        host=kw.get('host','localhost'),
        port=kw.get('port',3360),
        user=kw['user'],
        password=kw['password'],
        db=kw['db']
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        #接收一个event_loop实例
        loop=loop
    )
#封装sql SELECT语句为select函数
async def select(sql,args,size=None):
    log(sql,args)
    global __pool

    #_*_yield from 将会调用一个子进程，并直接返回调用结果
    #yield from 从连接池中返回一个子进程
    with (yield from __pool) as conn:
        cur=yield from conn.cursor(aiomysql.DictCursor)

        #执行sql语句
        #sql语句的占位符为？，MySQL的占位符为%s
        yield from cur.execute(sql.replace('?','%s'),args or ())

        #根据指定返回的size，返回查询结果
        if size:
            #返回size条查询结果
            rs=fetchmany(size)
        else:
            #返回所有查询结果
            rs=fetchall()
        yield from cur.close()
        logging.info('rows return:%s'%(len(rs)))

#封装INSERT UPDATE DELETE
#语句操作参数一样，所以定义一个通用的执行函数