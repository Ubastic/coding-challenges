import inspect

r = knock(knock)
_, l, o = [c.cell_contents for c in r.__closure__]

l()

r()