#BEAKJOON 14215
import sys

A = []
A = list(map(int,sys.stdin.readline().split()))
while sum(A) - max(A) <= max(A):
    A[A.index(max(A))] -= 1
print(sum(A)) 
