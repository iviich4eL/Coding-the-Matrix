from image import *
from plotting import *
data = file2image('img01.png')
# plot({x+y*(1j) for x in range(150) for y in range(150) if (data[x][y][1] < 120)},150)
pts = {x+y*(1j) for x in range(150) for y in range(150) if (data[x][y][1] < 120)}
plot({x for x in pts},150)