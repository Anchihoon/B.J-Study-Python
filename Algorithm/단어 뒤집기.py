#BAEKJOON 9093 
import sys

n = int(sys.stdin.readline())
for i in range(n):
    word = list(sys.stdin.readline().split())
    for j in range(len(word)):
        print(word[j][::-1],end=' ')
    print()