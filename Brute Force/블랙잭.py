#BAEKJOON 2798
import sys
import itertools

N, M = map(int,input().split())
A = list(map(int,sys.stdin.readline().split()))
A = list(map(sum,itertools.combinations(A,3)))

max = 0
for i in range(len(A)):
    if A[i] <= M and A[i] > max :
        max = A[i]
print(max)