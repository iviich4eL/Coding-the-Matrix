f = open('voting_record_dump109.txt')
mylist = list(f)

def list2int(lst): return [int(x) for x in lst] 
def create_voting_dict(strlist):
    voting_dict = dict()
    for lst in mylist:
        lst = lst.split()
        for i in range(2):
            lst.pop(1)
        name = lst.pop(0)
        voting_dict[name] = list2int(lst)
    return voting_dict

def dot_product(v, w) : return sum([ v[i] * w[i] for i in range(len(v))])
def policy_compare(sen_a, sen_b, voting_dict): 
    return dot_product(voting_dict[sen_a],voting_dict[sen_b])

def most_similar(sen, voting_dict): 
    senRes = 'None'
    mindset = -100000000 #policy_compare(sen,sen, voting_dict)
    for name in voting_dict:
        if name != sen and policy_compare(name, sen, voting_dict) >= mindset:
            mindset = policy_compare(name, sen, voting_dict)
            senRes = name
    return senRes

def least_similar(sen, voting_dict): 
    senRes = 'None'
    mindset = 100000000 #policy_compare(sen,sen, voting_dict)
    for name in voting_dict:
        if name != sen and policy_compare(name,sen, voting_dict) <= mindset:
            mindset = policy_compare(name,sen, voting_dict)
            senRes = name
    return senRes

def find_average_similarity(sen, sen_set, voting_dict):
    return  int(sum([policy_compare(sen, x, voting_dict) for x in sen_set]) / len(sen_set))

def create_democrate_set():
    f = open('voting_record_dump109.txt')
    mylist = list(f)
    democrates = list()
    for lst in mylist:
        lst = lst.split()
        if lst[1] == 'D':
            democrates.append(lst[0])
    democrates.sort()
    return democrates

def agree_with_democrats(voting_dict):
    flag = 0
    greatestSimilarity = 0
    resName = 'None'
    democrates = create_democrate_set()
    for name in voting_dict:
        averageSimilarity = find_average_similarity(name, democrates, voting_dict)
        if flag == 0:
            resName = name
            flag = 1
        else:
            if averageSimilarity > greatestSimilarity:
                greatestSimilarity = averageSimilarity
                resName = name
    return resName

def addN(v, w): return [v[n] + w[n] for n in range(len(v))]
def zero_vec(size): return [0 for x in range(size)]
def find_average_record(sen_set, voting_dict):
    res = zero_vec(len(myVotingDict['Warner']))
    for name in sen_set:
        res = addN(voting_dict[name], res)
    return [ x / len(sen_set) for x in res ]

def most_similar_to_average_Democrats(average_Democrat_record, voting_dict):
    res = -float('infinity')
    resName = 'None'
    for name in voting_dict:
        if dot_product(voting_dict[name], average_Democrat_record) >= res:
            res = dot_product(voting_dict[name], average_Democrat_record)
            resName = name
    return resName 


def bitter_rivals(voting_dict):
    res = float('infinity')
    resName = 'None'
    flag = 0
    for sen_a in voting_dict:
        for sen_b in voting_dict:
            if sen_a != sen_b and policy_compare(sen_a, sen_b, voting_dict) < res:
                res = policy_compare(sen_a, sen_b, voting_dict) 
                x = sen_a
                y = sen_b
    return (x, y)

def create_rivals_dict(voting_dict):
    return { name : int(0) for name in voting_dict}
def list2dict(D): return [ D[x] for x in D ]
def exchange_in_dict(D) : return { D[x] : x for x in D}
def find_max_in_dict(sen_dict):
    value_list = list2dict(sen_dict)
    value_list.sort()
    sen_dict = exchange_in_dict(sen_dict)
    return sen_dict[value_list[len(value_list) - 1]]

def most_political_opponents(voting_dict):
    treshold = 0
    sen_dict = create_rivals_dict(voting_dict)
    for sen_a in voting_dict:
        for sen_b in voting_dict:
            if sen_a != sen_b and policy_compare(sen_a, sen_b, voting_dict) < treshold:
                sen_dict[sen_a] = sen_dict[sen_a] + 1
    # print(sen_dict)
    return find_max_in_dict(sen_dict)


myVotingDict = create_voting_dict(mylist) 
average_Democrat_record = find_average_record(create_democrate_set(),myVotingDict)

print('Chafee most agrees with',most_similar('Chafee', myVotingDict))
print(least_similar('Santorum',myVotingDict),'most disagrees with Santorum')
print('Most agree with democrates:', agree_with_democrats(myVotingDict))
print('Most agree with democrates v2:', most_similar_to_average_Democrats(average_Democrat_record, myVotingDict))
print( most_political_opponents(myVotingDict),'has most political opponents')
# # print('Find average record:', average_Democrat_record)
# # myVotingDict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
# print('Bitter rivals: ', bitter_rivals(myVotingDict))
# test = {'apple' : 1, 'banana' : 0, 'orange' : 2}
# print(list2dict(test))
# print(find_min_in_dict(test))
# print(exchange_in_dict(test))
# print(test.values())
# M=-float('infinity')
# print(M)
# print('Schumer', 'Collins',policy_compare('Schumer', 'Collins', myVotingDict))
# print(create_democrate_set())
# print(create_voting_dict(mylist))
# print(policy_compare('Warner','Wyden', myVotingDict))
# print(most_similar('Schumer', myVotingDict))
# print(least_similar('Snowe', myVotingDict))
# print(most_similar('Collins', myVotingDict))
# print('Snowe', 'Collins',policy_compare('Snowe', 'Collins', myVotingDict))
# print('Collins','Snowe',policy_compare('Collins', 'Snowe', myVotingDict))
# print(myVotingDict['Warner'])