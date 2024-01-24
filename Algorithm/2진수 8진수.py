#BAEKJOON 1373
'''
n진수 -> 10진수
int(숫자, n진법)

10진수 -> n진수
2진수 bin(10진수 숫자)
8진수 oct(10진수 숫자)
16진수 hex(10진수 숫자)
나머지 진수로 바꾸는건 직접 짜야됨
'''
import sys

n = str(sys.stdin.readline())
print(oct(int(n, 2))[2:])