#BAEKJOON 2501
import sys

n, k = map(int,sys.stdin.readline().split())
A = []
for i in range(1,n+1):
    if n % (i) == 0 :
        A.append(i)

if k > len(A):
    print('0')
else :
    print(A[k-1])