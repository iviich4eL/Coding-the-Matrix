class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

# def zero_vec(D): return Vec(D,{})
def zero_vec(D): return Vec(D,{ d:0 for d in D})
D = {'A', 'B', 'C'}
print(zero_vec(D).f)