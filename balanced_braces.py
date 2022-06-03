i='{[]{()}}'
def balace_brace(inp):
    ip=list(inp)
    opn_br=['(','{','[']
    cl_br=[')','}',']']
    a,b=0,0
    for i in ip:
        if i in opn_br:
            a+=1
        elif i in cl_br:
            b+=1
        else:
            return None
    if a%2 or b%2 ==0:
        return ('True')
    else:
        return('False')


balace_brace(i)