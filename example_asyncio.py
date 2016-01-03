from WDIE import *
from pprint import pprint
import asyncio

@inject
def test(one, two="?"):
    print("one  : {}".format(one))
    print("two  : {}".format(two))

async def t1(d):
    print("Starting t1")
    await aget(d, "v")
    print("Got v and setting one")
    d["one"] = 1

async def t2(d):
    print("Starting t2")
    await aget(d, "one")
    print("Got one and setting two")
    d["two"] = 2

async def t3(d):
    print("Starting t3 and setting v")
    d["v"] = True

r = {}
tasks = [
    test(r),
    t1(r),
    t2(r),
    t3(r)
    ]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
pprint(r)
