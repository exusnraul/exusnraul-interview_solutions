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