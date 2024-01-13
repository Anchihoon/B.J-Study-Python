#BAEKJOON 11655
import sys

W = list(sys.stdin.readline())
for i in W:
    if ord(i) >= 65 and ord(i) < 95:
        if ord(i) <= 77:
            print(chr(ord(i) + 13),end='')
        else :
            print(chr(ord(i) - 13),end='')
    elif ord(i) <= 122 and ord(i) > 95:
        if ord(i) <= 109:
            print(chr(ord(i) + 13),end='')
        else :
            print(chr(ord(i) - 13),end='')
    else :
        print(i,end='')