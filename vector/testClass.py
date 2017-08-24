class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

v = Vec({'A','B','C'},{'A':0, 'B' :1 })
for d in v.D:
    if d in v.f:
        print(v.f[d])