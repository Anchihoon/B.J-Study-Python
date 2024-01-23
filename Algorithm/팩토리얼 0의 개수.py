#BAEKJOON 1676
import sys

def Factorial(x):
    if x > 1:
        return x * Factorial(x-1)
    else :
        return 1  

n = int(sys.stdin.readline())

S = str(Factorial(n))
cnt = 0
for i in S[::-1]:
    if i == '0':
        cnt += 1
    else :
        break
print(cnt)