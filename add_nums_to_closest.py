#this one is correct but can be modified to work with sorting algorithms like with pointer
a=[10,15,20,19,40,30,55]
b=100
def func1(arr,num):
    op={}
    # arr.sort()
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            # if arr[i]+arr[j] in range(num-5,num+5):
            op[arr[i]+arr[j]]=[arr[i],arr[j]]
    op1=[*op]
    # op1.sort()
    diff=1000
    min_=0
    for i in op1:
        temp=abs(i-num)
        if diff>temp:
            diff=temp
            min_=i
    return op[min_]

print(func1(a,b))


def func2(arr,num):
    arr.sort()
    diff=1000
    min_=0
    for i in range(len(arr)):
        temp=-1
        temp=abs(num-arr[i]+arr[temp])
        if arr[i]+arr[temp]<num and diff>temp:
            
            continue
        elif arr[i]+arr[temp]==num :
            return (arr[i],arr[temp])
        elif arr[i]+arr[temp]>num and diff>temp:
            temp-=1
            
print(func2(a,b))
            
            
    