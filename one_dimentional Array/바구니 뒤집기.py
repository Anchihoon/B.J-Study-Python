#BAEKJOON 10811
import sys

N, M = map(int,sys.stdin.readline().split())
A = []
for k in range(N):
    A.append(k+1)

for k in range(M):
    B = A.copy()
    i, j = map(int, sys.stdin.readline().split())
    c = j
    for l in range(i-1,c):
        A[l] = B[j-1]
        j = j - 1
print(A)        
