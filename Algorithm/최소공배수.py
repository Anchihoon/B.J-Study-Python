#BAEKJOON 1934
import sys
import math

#최대공약수 = Greatest Common Divisor
#최소공배수 = Least Common Multiple

n = int(sys.stdin.readline())
for i in range(n):
    A, B = map(int,sys.stdin.readline().split())
    print(math.lcm(A, B))