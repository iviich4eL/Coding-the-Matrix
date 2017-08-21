def mySum(L):
    current  = 0
    for x in L :
        current = current + x
    return current

input = [1,2,4,5,6,7,8,9,0]
print(mySum(input))