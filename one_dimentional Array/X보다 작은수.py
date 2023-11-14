#BAEKJOON 10871
import sys

N, X = map(int, sys.stdin.readline().split())
A = []
A = list(map(int, sys.stdin.readline().split()))

for i in range(0,N):
    if A[i] < X:
        print(A[i],end=' ')