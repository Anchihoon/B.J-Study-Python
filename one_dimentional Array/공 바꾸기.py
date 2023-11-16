#BAEKJOON 10813
import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for k in range(N):
    A.append(k+1)
for k in range(M):
    i, j = map(int, sys.stdin.readline().split())
    A[i-1], A[j-1] = A[j-1], A[i-1]
for k in range(N):
    print(A[k],end=' ')