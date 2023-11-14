#BAEKJOON 10810
import sys

N, M = map(int,sys.stdin.readline().split())
A = []
for l in range(N):
    A.append(0)
for l in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for p in range(i-1,j):
        A[p] = k
for l in range(N):
    print(A[l],end=' ')