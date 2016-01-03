# This project is licensed under the MIT License :
#
# Copyright (c) 2016 Nicolas "nicoxxl" Boudet
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import inspect
import types
import functools

def inject(func):
    assert callable(func)
    @functools.wraps(func)
    async def wrapper(res):
        sig = inspect.signature(func)
        args = []
        for foo in sig.parameters:
            args.append(await aget(res, foo))
        return func(*args)
    return wrapper


@types.coroutine
def aget(dic, value):
    while not value in dic:
        yield
    return dic[value]

def wloop(coros):
    coros = set(coros)
    discard = set()
    while coros:
        for c in coros:
            try:
                c.send(None)
            except StopIteration:
                discard.add(c)
        coros.difference_update(discard)
        discard.clear()
