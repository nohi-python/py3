import asyncio
from asyncio import get_event_loop
from unittest import TestCase

from www.common.db import orm
from www.model.models import User


async def test_select(loop):
    await orm.create_pool(loop, host='139.224.41.4', user='root', password='nohi1234', database='py_test')
    sql = 'select * from users'
    print('sql:%s' % sql)
    users = await orm.select(sql, [])
    for x in users:
        print(x)


async def test(loop):
    await orm.create_pool(loop, host='139.224.41.4', user='root', password='nohi1234', database='py_test')

    u = User(name='Test', email='20210609w@example.com', passwd='1234567890', image='about:blank')
    await u.save()


async def query_user(loop):
    await orm.create_pool(loop, host='139.224.41.4', user='root', password='nohi1234', database='py_test')
    use = await User.findAll()
    for x in use:
        print(x)


class TestWww(TestCase):
    def test_select(self):
        loop = asyncio.get_event_loop()
        get_event_loop().run_until_complete(test_select(loop))

    def test_db(self):
        loop = asyncio.get_event_loop()
        get_event_loop().run_until_complete(test(loop))

    def test_queryUser(self):
        loop = asyncio.get_event_loop()
        get_event_loop().run_until_complete(query_user(loop))
