from vector import * 

def add(u, v): return Vec(u.D, {d : getitem(u,d) + getitem(v,d)  for d in v.D})

u = Vec({'A','B','C'}, {'A': 5})
v = Vec({'A','B','C'}, {'A': 2,'B': 6})
w = add(u, v)

print(u.f)
print(v.f)
print(w.f)
