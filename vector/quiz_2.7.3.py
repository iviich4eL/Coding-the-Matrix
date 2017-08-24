from vector import *

def scalar_mul(v ,alpha): return Vec(v.D, {d : v.f[d]* alpha for d in v.f})
# def scalar_mul(v ,alpha): return Vec(v.D, {d : alpha*value for d,value in v.f.items()})

v = Vec({'A','B','C'}, {'A': 1})
alpha = 0
w = scalar_mul(v, alpha)
print(v.f)
print(w.f)