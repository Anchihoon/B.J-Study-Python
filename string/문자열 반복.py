#BAEKJOON 2675
import sys

t = int(input())
for i in range(t):
    r, S = sys.stdin.readline().split()
    r = int(r)
    for j in range(len(S)):
        for k in range(r):
            print(S[j],end='')
    print()