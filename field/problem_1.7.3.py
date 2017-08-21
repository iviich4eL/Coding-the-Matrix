def my_function_composition(f,g) : return { i : g[f[i]] for i in f }

f = { 0 : 'a', 1 : 'b' }
g = { 'a' : 'apple', 'b' : 'banana' }
d = my_function_composition(f,g)
print(d)