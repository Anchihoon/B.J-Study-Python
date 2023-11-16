#BAEKJOON 1546
import sys

N = int(input())
Grade = list(map(int,sys.stdin.readline().split()))
M = max(Grade)
sum = 0
for i in range(N):
    Grade[i] = Grade[i]/M*100
    sum = sum + Grade[i]
print(sum/N)