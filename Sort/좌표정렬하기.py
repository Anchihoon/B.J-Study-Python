#BAEKJOON 11650
import sys

n = int(sys.stdin.readline())
A = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    A.append(a)
A.sort(key = lambda x:(x[0],x[1]))
for i in range(n):
    print(*A[i])