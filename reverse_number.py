'''Reverse a given number , without type changing'''

def rev(n=int(input('Enter number:'))):
    n=n
    rev=0
    while n:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev

print(rev())

# 12345%10=5
#12345//10=1234