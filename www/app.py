# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:20:36 2017

@author: huang
"""

#Web app基于asyncio基础
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', 
                        content_type='text/html')

@asyncio.coroutine
def init(loop): #each loop stands for a user who has logged in the website
    app = web.Application(loop=loop)
    app.router.add_route('GET','/', index) #GET is a method which used to request data 
    					   #from the website
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1'
                                        , 9000) 
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
