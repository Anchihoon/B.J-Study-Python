#BAEKJOON 11005
#나머지연산을 하고 순서를 뒤집어 줘야함
import sys
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int,sys.stdin.readline().split())
ans = ''
while N != 0:
    ans += str(arr[N % B])
    N = N // B
print(ans[::-1])