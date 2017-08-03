# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:09:00 2017

@author: huang
"""

import orm
from models import User, Blog, Comment
import asyncio

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop = loop, user = 'root', password = '123qwe', db = 'awesome')
    u = User(name = '黄铭', email = 'test3@example.com', passwd = '1234567890',image = 'about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()