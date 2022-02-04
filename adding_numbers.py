#add the digits together of a given number 

def adding_digits(inp):
    n=inp
    num=0
    while n:
        dig=n%10
        num=dig+num
        n=n//10
    return num

print(adding_digits(12345))