def add2(v, w): return [v[0] + w[0], v[1] + w[1]]

firstVector = [4, 4]
secondVector = [-4, -4]
translation = [1, 2]

print("[4,4] = ", add2(firstVector, translation))
print("[-4,-4] = ", add2(secondVector, translation))
