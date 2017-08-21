def myMin(L):
    current  = L
    for x in L :
        current = L.remove(max(L))
    return current

input = [2,5,1,5,7,3,7,10]
print(myMin(input))