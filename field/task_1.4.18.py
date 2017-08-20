from plotting import plot
from math import pi
from math import e
S = [2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j]
M = [ x * (pow(e, (pi/4*1j))) for x in S ]
plot(M,4)