#sort numbers of an array

def bubla_Sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubla_Sort([1,4,6,5,45,34,2,3,4345,4]))


data_list=[1,2,3,4,5,65,66,34,23,423,42,2213,123,43,12,3,455,78,634,31,2312]
new_list=[]
while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)