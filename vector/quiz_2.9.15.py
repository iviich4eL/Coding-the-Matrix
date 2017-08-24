from vector import * 

def list_dot(u, v): return sum(u[i] * v[i] for i in range(len(u)))

def dot_product_list(needle, haystack): 
    s = len(needle)
    return [ list_dot(needle, haystack[i : i+s])  for i in range(len(haystack)-s+1) ]

# haystack = [1, -1, 1, 1, 1, -1, 1, 1,1]
# needle = [1, -1, 1, 1, -1, 1]

haystack = [1,2,3,4,5,6]
needle = [1,2,3]

result = dot_product_list(needle, haystack)

print(result)