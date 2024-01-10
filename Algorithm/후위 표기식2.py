#BAEKJOON 1935
'''
후위표기식
1. 피연산자를 스택에 넣음
2. 피연산자가 나오면 스택에서 값 두개 pop해서 계산
3. 계산한 값을 다시 푸시
'''
import sys

A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(sys.stdin.readline())
E = list(sys.stdin.readline().strip())
stack = []
N = []

for _ in range(n):
    N.append(int(sys.stdin.readline()))

for i in E:
    if i!='+' and i!='*' and i!='/' and i!='-' :
        stack.append(N[A.index(i)])

    elif stack:
        y = stack.pop()
        x = stack.pop()

        if i == '+':
            stack.append(x + y)

        elif i == '*':
            stack.append(x * y)
 
        elif i == '-':
            stack.append(x - y)

        elif i == '/':
            stack.append(x / y)


print('%.2f'%stack[0])