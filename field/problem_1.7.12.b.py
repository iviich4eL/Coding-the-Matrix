def transform(a, b, L) : return [ a * z + b for z in L ]

S = [2+1j]#,2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j]
print(S)
M = transform(1,0,S) # scale real part by two and the imginary part by three
print(M)