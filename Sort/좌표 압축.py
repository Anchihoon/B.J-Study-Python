#BAEKJOON 18870
import sys

n = int(sys.stdin.readline())
S1 = list(map(int,sys.stdin.readline().split()))

S2 = sorted(list(set(S1)))
dic = {S2[i]:i for i in range(len(S2))}

for i in S1:
    print(dic[i],end=' ')