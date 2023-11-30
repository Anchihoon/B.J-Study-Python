#BAEKJOON 9063
import sys

n = int(input())
X = []
Y = []

for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

a = max(X) - min(X)
b = max(Y) - min(Y)

print(a*b)
