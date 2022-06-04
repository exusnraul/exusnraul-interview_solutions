'''
•	Check if given number/string is palindrome.
'''

def palindrome(st):
    if isinstance(st,str) and st==st[::-1]:
        return ('String a Palindrome')
    elif isinstance(st,int) and str(st)==str(st)[::-1]:
        return ('Number a Palindrome')
    else:
        return 'Try Again'
    
palindrome(121)