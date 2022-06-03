import random


def gen_rand(x):
    a=random.randint(0,x)
    return a 

a=[gen_rand(a) for a in range(0,100)]
print(a)


def sorter(arr):
    dic={}
    for item in arr:
        if arr.count(item) not in dic.keys():
            dic[arr.count(item)]=[item]
        else:dic[arr.count(item)].append(item)
        
    print(dic)

sorter(a)