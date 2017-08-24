class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

def zero_vec(D): return Vec(D,{ d:0 for d in D})

def getitem(v, d): return v.f[d] if d in v.f else 0