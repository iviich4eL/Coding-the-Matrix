def makeInverseIndex(filename):
    f = open(filename)
    x = 0
    wordDict = dict()
    for line in f:
        string = str(line)
        string = string.split()
        for word in string:
            if word in wordDict:
                val = set()
                val = wordDict[word]
                val.add(x)
                wordDict[word] = val
            else:
                val = set()
                val.add(x)
                wordDict[word] = val
        x = x + 1
    return wordDict