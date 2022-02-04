#removing duplicates from a string/list

a='abcdacbdabe'
v=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,7,8,9,7,6,5,4,4,3]
count=0
c=[]
def remove_dups(a):
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    if type(a)==str:
        return ''.join(c)
    else:return c

b=remove_dups(a)
c=remove_dups(v)

print(b,c)