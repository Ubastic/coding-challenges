import operator as o
class Node:
    def __init__(s,*v):s.v = v
value=type('',(Node,),{'compute':lambda s:s.v[0]})
for n in 'add','sub','mul','truediv','mod','pow':
    f=lambda s,c=getattr(o,n):c(s.v[0].compute(),s.v[1].compute())
    __builtins__['global'+'s']()[n]=type('',(Node,),{'compute':f})