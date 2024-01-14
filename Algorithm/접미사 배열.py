#BAEKJOON 11656
import sys

S = sys.stdin.readline().strip()
arr = []
for i in range(len(S)):
    arr.append(S[i:])
arr.sort()
for _ in arr:
    print(_)