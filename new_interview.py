import time

# while True:
#     print('Hello World')
#     time.sleep(5)


l1=[10,20,10,30,40,10,20]
l2=[]
for item in l1:
    if item not in l2:
        l2.append(item)

print(l2)
a={}
for item in l1:
    c=l1.count(item)
    if item not in a.keys():
        a[item]=c

print(a)

'''
str1="he is anand and anand is from blore. and  Anand is good in python"
write a code to identify how many anand is there
'''
str1="he is anand and anand is from blore. and  Anand is good in python"
list_str=[x.lower() for x in str1.split(' ')]
print(list_str.count('anand'))

list_num=[1,4,6,7,212,435,76,87,3,123]
lis2=[]
while list_num:
    max_num=list_num[0]
    for i in list_num:
        if max_num<i:
            max_num=i
    list_num.remove(max_num)
    lis2.append(max_num)

print(lis2[2])


