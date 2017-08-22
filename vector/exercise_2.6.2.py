from plotting import plot
def scalar_vector_mult(alpha, v) : return [ alpha* v[n] for n in range(len(v))]
def add2(v, w): return [v[0] + w[0], v[1] + w[1]]


u = [1, 4]
v = [6, 3]

plot([add2(scalar_vector_mult(i/100., [5,-1]), [1, 4]) for i in range(101)],10)
plot([ scalar_vector_mult( i/100.,add2(scalar_vector_mult(i/100., [5,-1]), [1, 4]) for i in range(101)) for i in range(101)],10)
