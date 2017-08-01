from makeInverseIndex import *

def orSearch(inverseIndex, query):
    containAny = set()
    for i in query:
        if i in inverseIndex:
            containAny = containAny | inverseIndex[i]
    return containAny

query = ['banana', 'it', 'is']
A = orSearch(makeInverseIndex('banana.txt'), query)
print(A)
