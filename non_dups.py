'''
•	Get all non-duplicate elements of list. Consider list is very large
'''
a=[1,2,22,3,4,4,5,3,3,23,2,3234,23,4324,23,12,3,123,12,'sdasd','asdasd','asds']*100000
def nondups(arr):
    try:
        elements=list(set(arr))
        elements_dict={}
        for item in elements:
            if  arr.count(item) not in elements_dict.keys():
                elements_dict[arr.count(item)]=[item]
            else:
                elements_dict[arr.count(item)].append(item)
        return elements_dict[1]
    except KeyError as e:
        print('No Non-Duplicate Items')

nondups(a)