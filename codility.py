'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

a={1,2,3,4}
b={1,2,4,5,6}
# print(a-b)

print(a.difference(b))
def solution(A):
   a=frozenset(sorted(A))
   m=max(a)
   if m>0:
       for i in range(1,m):
           if i not in a:
              return i
       else:
          return m+1
   else:
       return 1
   
def solution(A):
    m = max(A)
    if m < 1:
       return 1

    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        return m + 1
    else:
        return min(D)