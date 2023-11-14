#BAEKJOON 10807
import sys
A = []
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
C = 0 
for i in range(0,N):
    if A[i] == M:
        C += 1
print(C)    

