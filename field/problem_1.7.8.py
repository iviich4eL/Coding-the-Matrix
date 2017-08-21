def myUnion(L):
    current  = set()
    for x in L :
        current = current | x
    return current

input = [{1,3},{1,2},{1,2,3},{5,3,4}]
print(myUnion(input))