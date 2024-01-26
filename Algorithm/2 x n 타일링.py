#BAEKJOON 11726
import sys
input = sys.stdin.readline

t = [0] * 1001
t[1] = 1
t[2] = 2

for i in range(3,1001):
    t[i] = t[i-1] + t[i-2]

n = int(input())

print(t[n]%10007)