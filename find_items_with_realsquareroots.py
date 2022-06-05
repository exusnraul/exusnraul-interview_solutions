a=[2,4,6,8,10,9,25,36,3,323,45,34]
import math
print(type(math.sqrt(8)))
print(list(map(lambda x:x if math.sqrt(x).is_integer() else None,a)))

list(map(int,filter(float.is_integer,map(math.sqrt,a))))

#Map and filter returns an object which is to be iterated upon and get the values

#Reduce Statement ites over iterable and gives a single output

from functools import reduce
a=[1,2,3,4,44,5,56,7,9]
print(reduce(lambda x,y:x if x>y else y, a))