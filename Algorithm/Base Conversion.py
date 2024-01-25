#BAEKJOON 11576
import sys
input = sys.stdin.readline

#10진수를 n진수로 변환하는 함수 Conversion()
def Conversion(x, a):
    A = []
    while x > 0:
        x, mod = divmod(x, a)
        A.append(mod)
    return A[::-1]


A, B = map(int,input().split())
n = int(input())
S = list(map(int,input().split()))
j =0
sum = 0
for i in S[::-1]:
    sum += i * (A**j)
    j += 1

for j in list(Conversion(sum, B)):
    print(j,end=' ')