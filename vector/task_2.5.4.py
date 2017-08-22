from plotting import plot
def scalar_vector_mult(alpha, v) : return [ alpha* v[n] for n in range(len(v))]

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]
plot([scalar_vector_mult(0.5, v) for v in L], 4)
plot([scalar_vector_mult(-0.5, v) for v in L], 4)