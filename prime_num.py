from ast import Num


def primenum():
    rng=int(input('ENter Range'))
    dic={'prime':[1,2],'not_prime':[]}
    count=2
    for i in range(3,rng+1):
        for j in range(2,i):
            if i%j==0:
                val=i
                dic['not_prime'].append(val)
                break
        else:dic['prime'].append(i)
    return dic

num=100
for i in range(2,num):
    if num%i==0:
        print('Its not a prime')
        break
else:
    print('Its a prime')