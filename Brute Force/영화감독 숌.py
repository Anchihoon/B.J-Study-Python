#BAEKJOON 1436
#cnt 를 계속 1씩 증가하면서 찾는다
import sys

n = int(sys.stdin.readline())
num = 0
cnt = 0

while True :
    if '666' in str(num):
        cnt += 1
        if cnt == n:
            break
        else :
            num += 1
    else :
        num += 1
print(num)