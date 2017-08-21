def transform(a, b, L) : return [ a * z + b for z in L ]

S = [1+1j,2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j]
print(S)
M = transform(1, 1j, S) # one unit up
print(M)
M = transform(1, -1, S) # one unit to the right
print(M)
M = transform(1j, 0, S) # rotate ninety degrees clockwise
print(M) 
M = transform(2, 0, S) # scale by two
print(M)
