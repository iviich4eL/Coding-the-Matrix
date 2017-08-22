from plotting import plot
def scalar_vector_mult(alpha, v) : return [ alpha* v[n] for n in range(len(v))]
def add2(v, w): return [v[0] + w[0], v[1] + w[1]]
def segment(pt1, pt2): return [ add2(scalar_vector_mult((alpha/100), pt1), scalar_vector_mult(1 - (alpha/100), pt2)) for alpha in range(100) ] 
    
pt1 = [3.5, 3]
pt2 = [0.5, 1]
res = segment(pt1, pt2)
plot([x for x in res],4)
