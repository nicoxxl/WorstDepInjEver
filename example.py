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
