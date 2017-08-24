from vector import *

def list2vec(L): return Vec(set(range(len(L))),{ i : L[i] for i in range(len(L))}) 

L = ['a','b','c','d','e']

print(list2vec(L).f)