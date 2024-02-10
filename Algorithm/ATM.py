#BAEKJOON 11399
import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
for i in range(1,n):
    A[i] = A[i] + A[i-1]
print(sum(A))