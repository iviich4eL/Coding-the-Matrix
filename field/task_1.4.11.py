from plotting import plot
def origin(x): return x - (2.5+1.5j)

S = [2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j]
M = [ origin(x) for x in S]
plot(M,4)