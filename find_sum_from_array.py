import time
def adder_dict(arr,var):
    start_time=time.perf_counter()
    a={}
    var=var
    for i in range(len(arr)):
        for j in range(0,len(arr)):
            new_var=arr[i]+arr[j]
            if new_var not in a:
                a[new_var]=[(i,arr[i]),(j,arr[j])]
            else:
                a[new_var].extend([(i,arr[i]),(j,arr[j])])
                
    # if var in a:
    #     print(a[var])
    end=time.perf_counter()
    print(start_time-end)

adder_dict([1,2,3,4,5]*100,5)



def adder_logic(arr,var):
    start_time=time.perf_counter()
    a={}
    var=var
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j]==var:
                # print(i,arr[i],j,arr[j])
                break
    end=time.perf_counter()
    print(start_time-end)
adder_logic([1,2,3,4,5]*100,5)