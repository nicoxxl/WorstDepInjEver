Worst Depedency Injection Ever
==============================

Well, it say it all.

What does it do ?
-----------------

It do dependency injection, with async/await (so it's compatible with asyncio).
But it facts, it's more a way for me to play with python than a serious project.


Example
-------

```python
from WDIE import aget, wloop
# Store all the provided ressources:
ressources = {}

async def t1(r):
  print(await aget(r, 1))
  r[2] = "Two"
async def t2(r):
  r[1] = "One"
  print(await aget(r, 2))

wloop((t1(ressources), t2(ressources)))
print(ressources)
```

Result :

```
One
Two
{1: 'One', 2: 'Two'}
```

See example*.py files.

Docs
----

http://benno.id.au/blog/2015/05/25/await1
