nums = [3,2,4]
target = 5


def adder(n,arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==n:
                return (i,j)
        

# print(adder(target,nums))

class A:
    def __init__(self,n,arr):
        self.arr=arr
        self.targ=n

    def adder(self):
        for i in range(len(self.arr)):
            for j in range(i+1,len(self.arr)):
                if self.arr[i]+self.arr[j]==self.targ:
                    return (i,j)
    

a=A(target,nums)
print(a.adder())


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


#Persistent
'''
employee
    id, name, age, gender, department, salary
    give departments with total Annual salary more than 1CR, for  people in range of age 30 to 35 and gender male.
'''

# select department from employee where salary > '1cr' Group by department having age between (30,35)  


inp='Immo sit sane nihil melius, inquam-nondum enim id quaero-, num propterea idem voluptas est, quod, ut ita dicam, indolentia?'
# print(inp.split(" "))
def word_count(inp):
    c=inp.split(' ')
    op={}
    for words in c:
        length_word=len(words)
        temp='Word'+"-"+str(len(words))
        if temp not in op.keys():
            op[temp]=1
        else:op[temp]=op[temp]+1
    return op

print(word_count(inp))



#Mirafra
# inp='AAHHGDHHJJJWHHH'
# def counter_of_letters(inp_str=str(input('Enter the string'))):
#     op={}
#     for item in inp_str:
#         if item not in op.keys():
#             op[item]=inp_str.count(item)

#     return op

# print(counter_of_letters())
#Return 3 numbers addded to the target from the list
inp_list=[3,5,6,7,9,1,2,4,3,6]

def adder_(inp,num):
    op={}
    for i in range(len(inp)):
        a=num-inp[i]
        for j in range(i,len(inp)-1):
            if inp[j]+inp[j+1]==a:
                print(inp[i],inp[j],inp[j+1])


adder_(inp_list,12)

# a=[1,2,3,4,[1,2,3,4,4]]
# import copy

# b=a.copy()
# b.append(6)
# b[4].append(6)
# print(a,b)

# copy.deepcopy

#GoVega
inp = 'my name is rahul'

op='rahul is name my'


# lis_1=inp.split(' ')
# lis_=[]
# lis_.extend((lis_1[3],lis_1[2],lis_1[0],lis_1[1]))
# # print(' '.join(lis_))

# def string_(inp):
#     lis=inp.split(' ')
#     di={}
#     for i in range(len(inp)):
#         di[i]=inp[i]
# import copy
# first = [1, 2, 3, 4, 5,[1,2,3,4]]
# second = first

# a=first.copy()

# a.append(6)
# b=copy.deepcopy(first)


# # copy.deepcopy()
# a[5].append(6)
# print(a)
# print(first)

# second.append(6)
# print(first)
# print(second)


inp=[1,2,31,2,4,3,2]
op={}
for i in inp:
    if inp.count(i) not in op.keys():
        op[inp.count(i)]=[i]
    else:
        op[inp.count(i)].append(i)

print(op[1])
lis_=[]
for i in inp:
    if i not in lis_:
        lis_.append(i)

print(lis_)

first = [1, 2, 3, 4, 5]
second = first
second.append(6)
print(first)
print(second)

# [12:36 PM] Devendra Shetty
#     names = ['Chris', 'Jack', 'John', 'Daman']
# print(names[-1][-1])


#Prsistent

# inp ='Strings to be reversed'

# lis_=inp.split(' ')

# lis_=[x[::-1] for x in lis_]

# print(' '.join(lis_))




# a = [1,2,3,4,5,6,7,8,9]
# print(a[-1:-5:-1])
# b=a
# import copy

# a=[1, 2, 3, 4, 5,[7,8,9]]
# b=a.copy()
# a.append(5)
# print(a)

# a.extend([7,8,9])

#****
# inp='ABCD'
# op=[]
# for i in range(len(inp)):
#     w=inp[i]
#     for j in range(len(inp)):


''''
emloyee - id,name,dept,salary


select * from employee where salary >(select salary from employee partition by salary where salary>avg(salary))

select * from employee self join employee as e on employee  where salary=salary and id
'''
'''
Questions(Persistant)
SSL,HTTPS,Handshake,API Headers and Responses,How a request response cycle works on the whole,
'''
# Wipro
'''input = aaabbbaabbcc
output = 3a3b2a2b2c'''
input = 'aaabbbaabbcc' #Not Completed
# def func1(inp):
#     count=1
#     op=''

#     val=inp[0]
#     for i in range(len(inp)):
#         for j in range(i+1,len(inp)):
#             if inp[i]==inp[j]:
#                 count+=1
            
#             else:op+str(count)+inp[i]

#     return op

# print(func1(input))
inp="abc def abd jgk abc gkjgk def abc"

# op={"abc":3, "def":2, "abd":1, ...}
# print(inp.split(' '))

def func2(inp):
    if isinstance(inp,str):
        temp=inp.split(' ')
    elif isinstance(inp,list):
        temp=inp
    else:
        raise ValueError("Input Only String or Lists as an input")
    op={}
    for item in temp:
        if item not in op:
            op[item]=temp.count(item)
        
    return op

print(func2(inp))

'''
emp,salary 

emp - id , name , details 
sal  - emp id(fk) ,id, salary 

select emp.name,sal.salary from emp left join sal on emp.id=sal.id  where sal.salary<max(sal.salary) limit 1 

Metaclass, Meta programming , Method Resolution Order , Design Patterns 
'''
'''CGI'''


i='{[]{()}}'

lid_=['(',')','{','}','[',']']

def balance(inp):
    temp=list(inp)
    print(temp)
    for item in temp:
        print(temp.count(item))
        if temp.count(item)%2!=0:
            print('Unbalanced')
            
    else:
        print('Balanced')

balance(i)
# print(set(i))

'''
NeosoftTechologies
Sourabh Soni16:43
Class User(models.Model):
    status = models.BooleanField(default=False)
    

Class UserProfile(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User)


Get all usersprofile for the users which have status True and age greater than 18 

sign in funtionality
'''
from copy import copy


L = [ {'x': 3}, {'x': 1}, {'x': 2} ]

# Sort it based on x value in ascending order. Expected output: [ {‘x’: 1}, {‘x’: 2}, {‘x’: 3} ]



def sort_(arr):
    temp_lis=[i['x'] for i in arr]
    temp_lis.sort()
    op=[]
    for i in temp_lis:
        op.append({'x':i})
    
    return op

print(sort_(L))

'''
Django in deep
cookie , session 
Login , signup
authentication
JWT authentication
Django ORM questions
Deployment of django projects
'''
'''
Ust Global
Aws EC2,Image builder, ELB et.c
'''
ip = "aaabbbaabbcc"
# op="3a3b2a2b2c"

def func1(inp):
    count=1
    op=''
    for i in range(len(ip)-1):
        if inp[i]==inp[i+1]:
            count+=1
        # elif inp[]
        else:
            op=op+str(count)+inp[i]
            count=1
            # continue
    op=op+str(count)+inp[i]
    return op

print(func1(ip)) 

'''
Happiest Minds
OOps concept - Abstarct classes,static methods,django sessions,authentication,caching,architecture
database concepts- Nosql vs SQL,How to optimise sql DB and No SQL , 
project description , how to migrate to AWS and all
Python questions
'''
#get rid of the duplicates withot using any internal function
a=[1,1,2,3,4,5,6,6,7,7]
def func1(arr):
    count=1
    op=[]
    for i in range(len(a)-1):
        if arr[i]==arr[i+1]:
            arr.remove(arr[i])
            arr.remove(arr[i+1])
        
        
    return arr

# print(func1(a))


b=[x*x for x in a]    
print(b)
'''
Aviso
Hitesh Soneta
Data structures concept
'''
#get the difference of degrees between minute and hour hand
'''
minute hand tranvels 6 deg every minute and Hour hand travels 30 deg every hour 
de is the degree per minute
a*30 is the hour hand multiplied by degree and b/2 is hour hand oves 1deg every 2 minutes
'''
#correct 
a,b=2,40
de=6
op=(b*de)-(a*30+b//2)
print(op)
#this one is correct but can be modified to work with sorting algorithms like with pointer
a=[10,15,20,19,40,30,55]
b=100
def func1(arr,num):
    op={}
    # arr.sort()
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j] in range(num-5,num+5):
                op[arr[i]+arr[j]]=[arr[i],arr[j]]
    op1=[*op]
    op1.sort()
    diff=1000
    min_=0
    for i in op1:
        temp=abs(i-num)
        if diff>temp:
            diff=temp
            min_=i
