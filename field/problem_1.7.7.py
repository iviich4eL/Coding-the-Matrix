def myConcat(L):
    current  = str()
    for x in L :
        current = current + ' ' + x
    return current

input = ['this', 'is', 'a', 'list', 'of', 'strings']
print(myConcat(input))