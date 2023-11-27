#BAEKJOON 2581
import sys

def search_prime(n):
    DEV = []
    for i in range(1,n+1):
        if n % (i) == 0 :
            DEV.append(i)
    if len(DEV) == 2:
        return 1
    else :
        return 0

M = int(input())
N = int(input())
A = []
for i in range(M,N+1):
    if search_prime(i) == 1:
        A.append(i)
if A == [] :
    print('-1')
else :
    print(sum(A))
    print(min(A))