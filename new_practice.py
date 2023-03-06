# 1.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.Example 1:Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].Example 2:Input: nums = [3,2,4], target = 6 Output: [1,2]Example 3:Input: nums = [3,3], target = 6 Output: [0,1]

def finding_indexes(arr,n):
    i = 0
    op1=[]
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==n:
            op=[i,j]
            op1.append(op)
            i+=1
        else:
            i=i+1
    return op1

print(finding_indexes([2,7,9,0],9))


#add the digits together of a given number 
def adding_numbers(n):
    num=0
    while n:
        dig=n%10
        num+=dig
        n=n//10
    return num

print(adding_numbers(327))



import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@timeit
def func():
    lis=[]
    for i in range(1000):
        lis.append(i)
    return lis

func()

#exception Handling
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    print("Result: ", y)
finally:
    print("Execution complete")

def primy(i,j):
    max_=max(i,j)
    min_=min(i,j)
    op={'prime':[]}
    for k in range(min_,max_):
        for l in range(2,k):
            if k%l ==0:
                break
        else:
            op['prime'].append(k)
            
    return op

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

# Define the child class that inherits from the parent class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Create an instance of the child class
my_dog = Dog("Fido", "Golden Retriever")

# Call methods on the instance of the child class
print(my_dog.name)      # Output: Fido
print(my_dog.species)   # Output: Dog
print(my_dog.breed)     # Output: Golden Retriever
print(my_dog.make_sound())  # Output: Woof!
