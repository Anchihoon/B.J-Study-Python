#BAEKJOON 17087
'''
N명을 찾아야되고 현재 나는 S에 있음
동생들의 위치는 A배열의 원소로
최대공약수를 구하는 문제
절댓값 함수 abs(숫자)
'''
import sys
import math

N, S = map(int,sys.stdin.readline().split())
A = list(map(int,input().split()))
for i in range(N):
    A[i] = abs(A[i] - S)

while len(A) > 1 :
    x = A.pop()
    y = A.pop()
    A.append(math.gcd(x, y))
print(*A)