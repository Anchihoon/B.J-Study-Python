#BAEKJOON 3009
import sys

X = []
Y = []

for j in range(3):
    a, b = map(int,sys.stdin.readline().split())
    X.append(a)
    Y.append(b)

for i in range(3):
    if X.count(X[i]) == 1:
        a4 = X[i]
    if Y.count(Y[i]) == 1:
        b4 = Y[i]
print(a4, b4)