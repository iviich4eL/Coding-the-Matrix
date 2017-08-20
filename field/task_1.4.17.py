# import the neccesary modules
from plotting import plot
from math import pi
from math import e
S = [pow(e,2*pi*(1j)/ (n + 1)) for n in range(20)] # use comprehension
plot(S,4)