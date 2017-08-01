from makeInverseIndex import *

def andSearch(inverseIndex, query):
    flag = True
    containAll = set()
    for i in query:
        if i in inverseIndex:
            if flag is True:
                containAll = inverseIndex[i]
                flag = False
            else :
                containAll = containAll & inverseIndex[i]
    return containAll

query = ['banana', 'it', 'is']
A = andSearch(makeInverseIndex('banana.txt'), query)
print(A)
