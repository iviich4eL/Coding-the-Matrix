def myProduct(L):
    current  = 1
    for x in L :
        current = current * x
    return current

S = [1,2,4,5,6,7,8,9]
print(myProduct(S))