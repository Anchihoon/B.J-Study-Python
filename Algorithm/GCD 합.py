#BAEKJOON 9613
#둘이 서로소이면 math.gcd()는 1을 return
import sys
import math

n =int(sys.stdin.readline())
for i in range(n):
    S = list(map(int,sys.stdin.readline().split()))
    sum = 0
    for j in range(1,len(S)):
        for k in range(j+1,len(S)):
            sum += math.gcd(S[j], S[k])
    print(sum)