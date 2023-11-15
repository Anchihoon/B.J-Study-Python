#BAEKJOON 11021
import sys

i = int(input())
for j in range(1,i+1):
    a, b = map(int,sys.stdin.readline().split())
    print('Case #',j,': ',a+b, sep='')
    