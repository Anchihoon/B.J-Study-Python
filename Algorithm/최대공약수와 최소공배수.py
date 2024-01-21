#BAEKJOON 2609
import sys
import math

A , B = map(int,sys.stdin.readline().split())
'''
#브루트 포스 알고리즘

#최대공약수 체크를 위한 변수 X
#A,B중 작은 값으로 X를 설정하고 1씩 줄여나감
if A > B :
    X = B
else :
    X = A
Y = 1 #최소공배수 체크를 위한 변수 Y

while A % X != 0 or B % X != 0:
    X -= 1

while Y % A != 0 or Y % B != 0:
    Y += 1

print(X,'\n',Y,sep='')
'''

#하지만 파이썬은 라이브러리를 지원한다.

print(math.gcd(A, B))

# lcm = Least Common Multiple(최소공배수)
print(math.lcm(A, B))