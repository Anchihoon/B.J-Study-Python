#BAEKJOON 10808
import sys

A = 'abcdefghijklmnopqrstuvwxyz'
B = [0] * 26

N = list(sys.stdin.readline().strip())
for i in N:
    B[A.index(i)] += 1
print(*B)