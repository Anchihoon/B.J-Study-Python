#BAEKJOON 9012
import sys

n = int(sys.stdin.readline())

for i in range(n):
    w = sys.stdin.readline()
    A = []
    for j in range(len(w)-1):
        if w[j] == '(':
            A.append(w[j])
        else:
            if A == []:
                A.append(w[j])
                break
            elif  A[len(A)-1] == '(':
                del A[len(A)-1]

    if A == []:
        print('YES')
    else :
        print('NO')