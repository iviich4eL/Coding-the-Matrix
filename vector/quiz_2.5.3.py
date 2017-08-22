def scalar_vector_mult(alpha, v) : return [ alpha* v[n] for n in range(len(v))]

vector = [0, 1, 2, 3]
alpha = 4
print(scalar_vector_mult(alpha, vector))