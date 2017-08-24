from vector import * 

def list_dot(u, v): return sum(u[i] * v[i] for i in range(len(u)))

u = [1,2,3,4,5] 
v = [0,1,2,3,4]

print(list_dot(u,v))