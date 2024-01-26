#BAEKJOON 16194
import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int,input().split()))

t = [0] * (n+1)
t[1] = P[0]

for i in range(2, n+1):
    t[i] = t[i-1] + P[0]
    for j in range(1, i+1):
        t[i] = min(t[i], t[i-j] + P[j-1])
    
print(t[n])