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
     return (op[min_])

'''
CGI
'''
'''
Given an integer array A of size N.

 

 

You have to pick exactly B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

 

 

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . 
you need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you picked.



Example Input
Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [1, 2]
 B = 1


Example Output
Output 1:

 8
Output 2:

 2


Example Explanation
Explanation 1:

 Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2:

 Pick element 2 from end as this is the maximum we can get
'''
#not correct
def solve(self, A, B):
        temp=0
        A.sort()
        if len(A)>B and B!=0:
            A=A.reverse()
            for i in range(B):
                temp+=A[i]
        else:
            pass
        return temp

'''
Datacultr
basic django questions, DRF, MODELS,ORM,and all
crate a Django Rest API CRUD Application
'''

'''
Comcast
Django arch, mixins,middleware,framework,models,authentication classes,Templates
Aws dynamodb -GSI,LST,TTL
How to authorize an app

'''
#find two friends in the network connected through a friend

network = {'friendships' :[['Marie', 'Lucas'], ['Lucas', 'Patsy'], ['Emma', 'Lucas'], ['Emma', 'Kevin'], ['Peter', 'Emma'], ['Peter', 'Lucas'], ['Peter', 'Julie'], ['Suzy', 'Tobias']]}
pool = set(map(frozenset, network['friendships']))
groups = []
while pool:
    groups.append(set(pool.pop()))
    while True:
        for candidate in pool:
            if groups[-1] & candidate:
                groups[-1] |= candidate
                pool.remove(candidate)
                break
        else:
            break
print(groups)
connected = {name: group for group in groups for name in group}
print(connected)
def is_connected_via_friendships_with(name1, name2):
    return name2 in connected.get(name1, ())

print(is_connected_via_friendships_with('Marie', 'Julie'))
print(is_connected_via_friendships_with('Julie', 'Tobias'))
print(is_connected_via_friendships_with('Julie', 'Frank'))

'''
capgemini 
Automation and testing
concept about vm , hypervisior,firewall , lynux deployment 
python - list vs tuple,set , frozen set uses ,
'''
# a=[x for x in range(10)]
# print(a)

# List = ['He', 'Loves', 'To', 'Code', 'In', 'Python']
# import random
# random.shuffle(List)
# print(List)

# a=(1,2,3,4,5,6,7)
# b=frozenset(a)
# print(a,b)
# b.add(5)

# import json
# a={'a':1,'b':2}
# b=json.dumps(a)
# print(b)
# c=json.loads(b)
# print(type(a),type(b),type(c))

# a='abcdefgh'
# # print(a[:5:2])

# a=[1,2,3,4]
# print(a[:2])
            
''''
Birla Soft
AWS- EC@, Load Balancer,Auto Scaling, Subnet , Lambda, what to do for more than 15 minutes,sqs,sns,
sql
'''

data={
    "class_id": "test0001",
    "students": [{
        "student_id": "xxxx",
        "student_name": "AAAABBBCCC",
        "student_gpa": 123
    }]
}


import pandas as pd
import urllib
import boto3
import csv

client=boto3.
url='dummy.com/api'
data=data
print(type(data))

with open('temp.csv',r+) as file:
    file.write(data)
    file.save()

client.

''''
tableA=emp id,name,salary
table2=empid,dept name
join get all the cols sal gt than 10k desc
'''

SALARY='''
select * from table1 as tb1 full outer join table2 as tb2  on tb1.emp_id=tb2.emp_id where tb1.salary>10,000
'''
'''
LNT TEch Services
Memory Management in python,Multithreading , Multi processing, Pros cons , GIT questions
'''
'''
Josephus problem
There was a group of 41 Jewish soldiers surrounded by Roman army, and they didn't want to get caught. So, they sat down in a circle and came up with an algorithm. Everybody had a sword, and starting from person #1 in the circle, everybody will kill the next living person on the left. So, #1 will kill #2. #3 will kill #4, #5 will kill #6 and so on. The last living person will have to commit suicide to avoid getting caught by Romans.

The soldier called Josephus preferred to be caught over committing suicide. So, in the group of 41 soldiers, he chose the location where he will be the last person living.

Write a program to figure out, in a group of given N people, where should Josephus sit to live at the end of all internal killing.

There is a mathematical solution to this problem. But, your program should use the brut force method to find the position. The output of the program may look like this:

Solving Josephus problem for 5 soldiers:
1 kills 2
3 kills 4
5 kills 1
3 kills 5
Josephus should sit on position# 3
'''
#Solutin Not provided as I cannot do it 

'''
Mouri Tech -- Rejected Average performance
Python Basics,
AWs Basics
'''
input=[2,5,6,2,3,6,5,6,8,0,9,6]
#highest Repeated Number

def func1(inp):
    op={}
    for item in inp:
        if inp.count(item) not in op.keys():
            op[inp.count(item)]=[item]
        else:
            if item not in op[inp.count(item)]:
                op[inp.count(item)].append(item) 
    a=[*op]
    a.sort()
    return (f' Total count is  {a[-1]} and number is {op[a[-1]]}')

print(func1(input))

# print(input.count(6))

'''
NTT
Devops concepts, How CI/CD works , DOCKER Kubernetes , Python basics,OS module,jsonpath ,API concepts,
How to safeguard APIs,Deployment strategies,MongoDb questions, System Design Concepts and scaling DB

tip - RabbitMQ,ELK,System Design concepts , Linux shell and SQL and Automation with Python,
Mainly OS,Shutil,JSONpath and scripting
'''
mylist = ["a", "b", "a", "c", "c"]
print(list(set(mylist)))
mylist = list(dict.fromkeys(mylist))
'''
Suez Water Technologies
Python basic questions , AWSbasicquestion , project architecture
screening round
'''
inp='python'
# print(inp[::-1])
def func(inp):
    op=''
    temp=-1
    lis_=list(inp)
    for i in range(len(lis_)):
        op+=lis_[temp]
        temp-=1
    return op

print(func(inp))
'''
CERNER INTERVIEW
Python -- Map , filter ,reduce with example. Iterator , Generator concepts with example and output data types type
class vs static method 
coding question - Use boto3 and perform CRUD on s3 bucket and Dynamodb 
use map or filter and filter out a list having pure sq rt of numbers provided.
'''
# import boto3

# client=boto3.clint(s3)
# bucket_name='test'
# def test():
#     file_name=

import math
inp=[1,4,5,8,9,20,25]
filter((lambda x :  a for a in x if type(math.sqrt(a))==int),inp)


@counter_decorator
def adder_(arr):
    op=[]
    while arr:
        min_=arr[0]
        for items in arr:
            if items<min_:
                min_=items
        arr.remove(min_)
        op.append(min_)
    return op
arr=[5,4,9,4,5,8,9,7,2,5,4,7,8,9,6,2,4,7,8,7]*1000
print(adder_(arr))
def counter_decorator(func):
    import time
    def wraper(*args):
        start=time.perf_counter()
        func(*args)
        end=time.perf_counter()
        return func
    return wraper
'''
Tech Mahindra
Python basic questions  - python language, core and all list/tuple/set 
'''
x='RRR'

op=lambda x: True if x[::-1]==x else False
print(op(x))

'''
Sopra Steria
AWS - Lambda whole (Env Variables,autoscale feature,Concurrency),Api gateway , security of API,S3 events ,Deployment problems with dependency
Lambda versioning, Cloudwatch USes,Serverless advantages ,DynamoDB uses,Architecture,Advantages.
'''
'''
KPMG
employee - emp_id,dept_id,name,...
department -  dept_id , dept_name

select d.dept_name , count(e.name) as total_employee from employee as e left join department as d on e.dept_id=d.dept_id having e.dept_id = d.dept_id

dept_name , count

emp_id,emp_nm,dept_name,salary

select dept_name , count(*) from emp group by (dept_name) having salary > 20,000

'''

'''
Caterpiller -- 3rd Party
Api Based Questions,Rest Based questions, what is REST why it is used , Oauth and session Based authentication
'''
# Invert a dict
inp={'a':1,'b':2,'c':3}

op={val:key for key,val in inp.items()}

print(op)
#create a range generator 
def gen(start,stop,step=1):
    ranger=stop
    count=0
    try:
        while ranger:
            count+=1
            yield count
            if count==stop:
                break
    except error as e:
        return None

'''
KPMG - IOT Services . AWS EC2,LAmbda,IOTCORE , Sensor type,IOT devices and uses
'''
'''
Suez - Final Round
Raindrop electricity generation has previously been employed as a form of microgeneration to power houses and small water purification systems –
 by capturing and funnelling rainwater to drive small turbines. 
'''

'''
CGI -- next round Monday with client
AWS concepts
'''
def func1(file_name):
    with open(file_name,'r') as file:
        data = file.readlines()

    print(data)
    op={}
    op_=[]
    for items in data:
        temp=items.split()
        op_.extend(temp)


    for item in op_:
        if op_.count(item) not in op.keys():
            op[op_.count(item)] = [item]
        else:
            op[op_.count(item)].append(item)

    return op 

print(func1('test.txt'))
'''
NTT data - associate architect
System Design ... Design a system Like Uber
'''
'''
Capgemini 
AWS concepts-- Python Basic Questions,Django , Show OOps concepts with programming
'''
def func1(file_name):
    with open(file_name,'r') as file:
        data = file.readlines()

    print(data)
    op={}
    op_=[]
    for items in data:
        temp=items.split()
        op_.extend(temp)


    for item in op_:
        if op_.count(item) not in op.keys():
            op[op_.count(item)] = [item]
        else:
            op[op_.count(item)].append(item)

    return op 

print(func1('test.txt'))
'''
Capgemini
'''
# class A():
#     def __init__(self,a):
#         self.a=a
#     def func1(self):
#         print(f'This is an arg={self.a}')

# # class B():
# #     pass
    
# class C(A):
#     def func2(self,a):
#         print('Inherited from A')
#         A.func1(self.a)

# test=C
# test.func2(5)

import time
def deco(func):
    def wrapper(*args):
        start=time.perf_counter()
        func(*args)
        end=time.perf_counter()
        print(f'Total time taken {end-start}')
    return wrapper
@deco
def func1(n):
    op=[]
    for i in range(n):
        op.append(i**2)

func1(10000)

'''
CGI- Final Client Round -- Data analytics
RDBMS questions maily with join 
'''
'''
table : employee
id|name 
100|praveen 
200|naveen 
300|kiran 
400|Kishta

table : dept 
id|dept 
300|A 
400|B 
500|A 
600|B 
700|C
question from full outer join and Right Join
'''

{ "distance": { "text": "227 mi", "value": 365468 }, "duration": { "text": "3 hours 54 mins", "value": 14064 }, "status": "OK" }

data={
  "destination_addresses": [
    "Washington, DC, USA",
    "Philadelphia, PA, USA",
    "Santa Barbara, CA, USA",
    "Miami, FL, USA",
    "Austin, TX, USA",
    "Napa County, CA, USA"
  ],
  "origin_addresses": [
    "New York, NY, USA"
  ],
  "rows": [{
    "elements": [{
        "distance": {
          "text": "227 mi",
          "value": 365468
        },
        "duration": {
          "text": "3 hours 54 mins",
          "value": 14064
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "94.6 mi",
          "value": 152193
        },
        "duration": {
          "text": "1 hour 44 mins",
          "value": 6227
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,878 mi",
          "value": 4632197
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 151772
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,286 mi",
          "value": 2069031
        },
        "duration": {
          "text": "18 hours 43 mins",
          "value": 67405
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,742 mi",
          "value": 2802972
        },
        "duration": {
          "text": "1 day 2 hours",
          "value": 93070
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,871 mi",
          "value": 4620514
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 152913
        },
        "status": "OK"
      }
    ]
  }],
  "status": "OK"
}

new_data=data['rows'][0]['elements']
# print(new_data)
op=[]

for items in new_data:
    temp_=[]
    fil_dt=''
    temp_1=items['distance']
    temp_2=items['duration']
    temp_.extend([str(x) for x in temp_1.values()])
    temp_.extend([str(x) for x in temp_2.values()])
    temp_.append(items['status'])
    fil_dt='|'.join(temp_)
    op.append(fil_dt)
# print(temp_)
print(op)
import pandas as pd
df=pd.DataFrame(op)
print(df)
df.to_csv('line.csv')
url='https://hackersandslackers.com/extract-data-from-complex-json-python/'
def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

print(json_extract(data,'text'))
'''id|name|manager_id 
1|praveen|2 
2|Murali|3 
3|Ketav|4 
4|Kishta|null 
6|Naveen|3
Show items with who are managers
select t1.name from table t1 self join table t2 where t1.id=t2.manager_id '''
'''
Capgemini - Client Samsung Full Stack Interview
Q-Questions about API and solutions to reading dfferent data types
'''
''''
int arr -+ find largestcont subarray containing the sum
'''


# def func1(arr):
#     temp=0
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i]<0:break
#             else:

# Python program to find maximum contiguous subarray
 
def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 
# Driver function to check the above function
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))

'''
Write a method to generate an infinite sequence of number. This should not cause memory overflow.
'''    
def func():
    a=0
    while True:
        yield a
        a+=1

for i in func():
    print(i, end=" ")
# puzzles - 3 bulbs one try which one connected to which
#             insect probem
'''
There is a room with a door (closed) and three light bulbs. Outside the room, there are three switches, connected to the bulbs. You may manipulate the switches as you wish, but once you open the door you can’t change them. Identify each switch with its bulb. All bulbs are in working condition.
Solution:
Let the bulbs be X, Y, and Z 
Turn on switch X for 5 to 10 minutes. Turn it off and turn on switch Y. Open the door and touch the light bulb. 
1. the light is on from the bulb, it is Y 

Now we will check other two off bulbs 
2. the bulb which is hot, it is X 
3. the bulb which is cold, it is Z  
'''
'''
Genpact -Python + AWS+SQL
Multithread,Multiprocess,Decorator,Web working,Api ,Statefull vs stateless
'''
# fibonacci series Generator
def func_gen(n):
    a,b=1,0
    while n:
        yield a
        a,b=b,b+a
        n-=1

for i in func_gen(10):
    print(i)
''''
emp - id,name,salary,city
emp having sal more tn 10k each city count
'''
'''
select city,count(*) from emp where salary > 10k group by city order by salary
'''
'''
Infocepts L1 - The worst interview Till Data
How to make your Apis Threadsafe , What is Multithreading and how it is implemented , What is OOps ,What is Polymorphism 
Give Example,What is Api Gateway give steps to create APIs , What is Lambda trigger, 
'''
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = ''
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)

'''    
Write a query to retrieve the EmpFname and EmpLname in a single column as “FullName”. The first name and the last name must be separated with space.
   
Write a query to fetch all employees who also hold the managerial position.

# '''
# A0 ={'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4} # the order may vary
# A1 = range(0, 10)
# A2 = []
# A3 = [1, 2, 3, 4, 5]
# A4 = [1, 2, 3, 4, 5]
# A5 =
# A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

'''
Calsoft - Python Based Interview
Basic to Advance Questions, OOPs concepts and prrofs
'''
l=[1,2,3,4,5]
m=l
# m.append(6)
print(l)
print(m)

import copy
m=copy.copy(l)

m.append(6)
print(l,m)
l=10
m=l
m=10

def deco(func):
    def wrapper(s):
        a=str.title()
        func(s)
        print(a)
    return wrapper
@deco
def func(s):
    print(s)

func('my name is rahul')

data="Nory was a Catholic because her mother was a Catholic,and Nory's mother was a Catholic because her father was a Catholic,and her father was a Catholic because his mother was a Catholic,or had been"

def func2(data):
    op={}
    data=data.replace(',',' ')
    string_=data.split()
    for i in string_:
        temp=string_.count(i)
        if i not in op.keys():
            op[i]=temp
    return op

print(func2(data))    
#Create A Generator with iter and next method included
class ManualGenerator():
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.op=[]
    def op(self):
        a=self.start
        while True:
            a+=1
            self.op.append(a)
            if a==self.end:break
    def __iter__(self):
        self.op
'''
UST Global-- Django related questions
Router, DRF framework,API building techniques
'''
l = [2,4,8,16,32, 7, 3, 9, 64, 27, 81, 39];

# figure out the pythagorean triplet from the above list
# a2 + b2 = c2
# Not solved
'''
Asteria Aerospace -- Basic Django Questions, Middlewares,Authentication,Manage.py advance questions
Basic Python questions
'''

lis=[1,2,3,4,5]
a=list(map(lambda x:x*x , lis))
print(a)

lis2=[1,2,3,4,5,6,7,8,9]

b=list(filter(lambda x:x if x%2==0 else None,lis2))
print(b)

c='quick brown fox jumps over a lazy dog'
d='quick {0} fox {1} over a {2} dog'.format('brown','{}','lazy')
op=d.format('jumps')
print(d)
'''
Nokia - Python Basic Questions
List,tuples,sets,dicts
Feedback - No practical Experience
SQL Update,insert and select methods
'''
'''
CGI- Python Basics , List,Tuple,set,DB,Django,REST,AWS and all
'''
import copy
a=[1,2,3,4,5,[7,8,9]]
c=copy.copy(a)

c[5].append(6)
print(a,c)

for i in range(10):
    # for j in range(i):
    print('* '*i)

'''
[4:30 PM] Hosagowdar, Siddanagouda B
Input: Toonandmoon
Max is 'o'
Input: MeenaReen
Max is 'e'
'''
ip='Toonandmoon'
def func1(inp):
    a=list(inp)
    op={}
    for i in a:
        temp=a.count(i)
        if temp not in op.keys():
            op[temp]=[i]
        else:
            op[temp].append(i)
    op1=list(set(op[max([x for x in op.keys()])]))
    return f'Max is:{op1[0]}'

print(func1(ip))

op=user.filter(date='ddmmyy')
'''
Mphasis - Python# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

1.top two maximum number without using predefined function 
2. highest repeated character and its count in a string
'''
def func1(arr):
    maximum=arr[0]
    op=[]
    for i in arr:
        if i>maximum:
            maximum=i
            op.append(maximum)
            arr.remove(maximum)
    return f'The maximum two numbers are {op[0]} and {op[1]}'
ip=[4,6,2,9,2,5,9]
print(func1(ip))

def func2(input):
    op={}
    ip=input.split()
    for i in ip:
        temp=ip.count(i)
        if temp not in op.keys():
            op[temp]=[i]
        else:
            op[temp].append(i)
    return op[max([*op])]
input='My Name is Name Rahul'
print(func2(input))
#Stopped iving Interviews Joined Persistent
