def my_filter(L, num) : return [x for x in L if (x % num !=0)]

list = [1,2,4,5,7]
num = 2

print(my_filter(list, num))