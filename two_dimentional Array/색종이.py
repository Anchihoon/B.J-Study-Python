#BAEKJOON 2563
import sys

A = [[0 for i in range(101)] for j in range(101)]
N = int(input())
for i in range (N):
    x, y = map(int,sys.stdin.readline().split())
    for j in range(x,x+10):
        for k in range(y, y+10):
            A[j][k] = 1

sum = 0
for i in A:
    sum += i.count(1)
print(sum)