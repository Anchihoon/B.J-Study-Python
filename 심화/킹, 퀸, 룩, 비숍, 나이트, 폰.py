#BAEKJOON 3003
#킹1개, 퀸1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
import sys
P = list(map(int, sys.stdin.readline().split()))
for i in range(2):
    print(1 - P[i],end=' ')
for i in range(2,5):
    print(2 - P[i],end=' ')
print(8 - P[5])