dict = { 0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E',
         5 : 'F', 6 : 'G', 7 : 'H', 8 : 'I', 9 : 'J',
         10 : 'K', 11 : 'L', 12 : 'M', 13 : 'N', 14 : 'O',
         15 : 'P', 16 : 'Q', 17 : 'R', 18 : 'S', 19 : 'T', 
         20 : 'U', 21 : 'V', 22 : 'W', 23 : 'X', 24 : 'Y', 
         25 : 'Z', 26 : 'space' }
# for i in dict: 
#     print(dict[i])
def bin2int(x) : return int(x, base = 2)
cyphertext = "10101 00100 10101 010011 11001 00011 01011 10101 00100 11001 11010"
cyphertext = cyphertext.split()
print(cyphertext)
for i in cyphertext:
    print(dict[bin2int(i)], end=" ")
# print(cyphertext)