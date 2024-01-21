#BAEKJOON 1978
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

n = int(input())
A = []
B = list(map(int,sys.stdin.readline().split()))
for i in range(len(B)):
    if search_prime(B[i]) == 1:
        A.append(B[i])
print(len(A))