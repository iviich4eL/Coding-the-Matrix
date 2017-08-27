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
        if name != sen: 
            policyComp = policy_compare(name,sen, voting_dict) 
            if policyComp > mindset:
                mindset = policyComp
                senRes = name
    return senRes

def least_similar(sen, voting_dict): 
    senRes = 'None'
    mindset = 100000000 #policy_compare(sen,sen, voting_dict)
    for name in voting_dict:
        if name != sen: 
            policyComp = policy_compare(name,sen, voting_dict) 
            if policyComp < mindset:
                mindset = policyComp
                senRes = name
    return senRes

def find_average_similarity(sen, sen_set, voting_dict):
    return  int(sum([policy_compare(sen,x, voting_dict) for x in sen_set]) / len(sen_set))

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

def addN(v, w): [v[n] + w[n] for n in range(len(v))]
def zero_vec(size): return [0 for x in range(size)]
def find_average_record(sen_set, voting_dict):
    res = zero_vec()
    return int( sum ([addN(voting_dict[name], res) for name in sen_set]) / len(sen_set))

myVotingDict = create_voting_dict(mylist)
print('Most agree with democrates:', agree_with_democrats(myVotingDict))

# print('Chafee most agrees with', most_similar('Chafee', myVotingDict))
# print(least_similar('Santorum',myVotingDict),'most disagrees with Santorum')
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