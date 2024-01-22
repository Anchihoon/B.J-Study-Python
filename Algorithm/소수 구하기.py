#BAEKJOON 1929
import sys

def prime(x):
    if x == 1:
        return False
    for i in range(2,int(x**(1/2)) + 1):
        if x % i == 0:
            return False
    return True 
        
M, N = map(int,sys.stdin.readline().split())
for i in range(M,N+1):
    if prime(i) == True:
        print(i)