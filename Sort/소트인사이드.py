#BAEKJOON 1427
import sys

N = sys.stdin.readline()
A = []
for i in range(len(N)-1):
    A.append(int(N[i]))
A.sort(reverse = True)
for i in range(len(A)):
    print(A[i],end='')