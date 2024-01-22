#BAEKJOON 10872
import sys

def Factorial(x):
    if x > 1:
        return x * Factorial(x-1)
    else :
        return 1  

n = int(sys.stdin.readline())
print(Factorial(n))