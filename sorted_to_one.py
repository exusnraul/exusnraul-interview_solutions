'''
Create a new list which is pre sorted from other two sorted lists
'''
a=[1,2,3]
b=[11,41,51]
c=[]
size_1 = len(a)
size_2 = len(b)
  
res = []
i, j = 0, 0
  
while i < size_1 and j < size_2:
    if a[i] < b[j]:
      res.append(a[i])
      i += 1
  
    else:
      res.append(b[j])
      j += 1
  
res = res + a[i:] + b[j:]