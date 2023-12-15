#BAEKJOON 11651
import sys

n = int(sys.stdin.readline())
A = []
for i in range(n):
    x = list(map(int,sys.stdin.readline().split()))
    A.append(x)

A.sort(key = lambda x : (x[1], x[0]))
for i in range(n):
    print(*A[i])