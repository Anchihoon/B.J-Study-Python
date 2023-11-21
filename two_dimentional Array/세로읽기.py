#BAEKJOON 10798
import sys

A = [[-1 for i in range(15)] for  j in range(5)]
for i in range(5):
    N = sys.stdin.readline()
    for j in range(len(N)):
        A[i][j] = N[j]
cnt = 0
i = 0
j = 0
while True:
    if A[i][j] != -1 and A[i][j] != '\n':
        print(A[i][j],end='')
        i += 1
        cnt = 0
    else :
        cnt += 1
    if i == 5:
        i = 0
        j += 1
    if cnt == 5:
        break
