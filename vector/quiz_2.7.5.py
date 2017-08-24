from vector import *

def neg(v): return Vec(v.D, {d : -1 * v.f[d] for d in v.D })

v = Vec({'A', 'B','C' }, { 'A': 1,'B' : 2,'C':3 })

print(v.f)
print(neg(v).f)