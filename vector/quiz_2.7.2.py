from vector import *

def getitem(v, d): return v.f[d] if d in v.f else 0

v = Vec({'A','B','C'},{'A':1})
print(getitem(v, 'A'))