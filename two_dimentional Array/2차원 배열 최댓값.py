#BAEKJOON 2566
import sys

A = []

for row in range(9):
    r = list(map(int,sys.stdin.readline().split()))
    A.append(r)
Max_A = max(map(max, A))
print(Max_A)
i,j = [(i,j) for i in range(9) for j in range(9) if A[i][j]==Max_A]
print(i, j)