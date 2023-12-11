#BAEKJOON 2839
'''
1. 5로 나누어떨어지는경우
2. 최소한의 3과 최대한의 5의 조합으로 떨어지는경우
3. 3으로 나누어 떨어지는 경우
4. 안되는 경우
'''
import sys

n = int(sys.stdin.readline())

if n % 5 == 0:
    print(n // 5)
else : 
    k = 0
    while n > 0 :
        n -= 3
        k += 1
        if n % 5 == 0:
            print(n // 5 + k)
            break
        elif n == 1 or n == 2:
            print('-1')
            break
        elif n == 0:
            print(k)
            break