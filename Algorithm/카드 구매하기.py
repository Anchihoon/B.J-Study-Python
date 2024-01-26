#BAEKJOON 11052
import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int,input().split()))

t = [0] * (n+1)

for j in range(1,len(P)):
    t[j] = P[j-1]

for i in range(2, n+1):
    for j in range(1, i+1):
        t[i] = max(t[i], t[i-j] + P[j-1])
        #본인은 왜 t[j]더하는게 아니라 P[j-1]을 더해야되는지 모르겠음
        #t[j]에 P[j-1]값을 다 복사해서 넣었는데 왜?????
    
print(t[n])