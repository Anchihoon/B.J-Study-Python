#BAEKJOON 1181
import sys

#입력, 배열에 추가
n = int(sys.stdin.readline())
A = []
R = []
for i in range(n):
    A.append(sys.stdin.readline().strip())

#중복 삭제
for i in A :
    if i not in R:
        R.append(i)

#정렬
R.sort()
R.sort(key = len)
for i in R:
    print(i)