#BAEKJOON 5073
import sys

while True:
    A = []
    A = list(map(int,sys.stdin.readline().split()))


    if A[0] == 0 and A[1] == 0 and A[2] == 0 :
        break
    if sum(A) - max(A) <= max(A) :
        print('Invalid')  
    else:
        if A[0] == A[1] and A[1] == A[2]:
            print('Equilateral')
        elif A[0] == A[1] or A[1] == A[2] or A[2] == A[0]:
            print('Isosceles')
        else :
            print('Scalene') 