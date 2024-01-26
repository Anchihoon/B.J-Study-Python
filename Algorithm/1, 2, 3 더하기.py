#BAEKJOON 9095
import sys
input = sys.stdin.readline

n = int(input())

t = [0] * 11
t[1] = 1
t[2] = 2
t[3] = 4
for i in range(4,11):
    t[i] = t[i-1] + t[i-2] + t[i-3]

for _ in range(n):
    m = int(input())
    print(t[m])