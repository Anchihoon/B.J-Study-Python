#BAEKJOON 15552
import sys

i = int(input())
for j in range(i):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)