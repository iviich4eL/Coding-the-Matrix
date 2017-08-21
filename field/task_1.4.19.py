from plotting import *
from image import *
from math import pi
from math import e
data = file2image('img01.png')
pts = {x+y*(1j) for x in range(150) for y in range(150) if (data[x][y][1] < 120)}
M = [ x * (pow(e, (pi/4*1j))) for x in pts ]
plot(M ,4)