#BAEKJOON 2738
import sys

A, B = [], []

N, M = map(int,sys.stdin.readline().split())
for i in range(N):
    r = list(map(int,sys.stdin.readline().split()))
    A.append(r)
for i in range(N):
    r = list(map(int,sys.stdin.readline().split()))
    B.append(r)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j],end=' ')
    print()