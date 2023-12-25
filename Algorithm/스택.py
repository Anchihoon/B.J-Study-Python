#BAEKJOON 10828
import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    N = sys.stdin.readline().split()
    
    if N[0] == 'push':
        stack.append(N[1])
    
    elif N[0] == 'pop':
        if stack == []:
            print('-1')
        else :
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
    
    elif N[0] == 'size':
        print(len(stack))

    elif N[0] == 'empty':
        if stack == []:
            print('1')
        else :
            print('0')

    elif N[0] == 'top':
        if stack == []:
            print('-1')
        else:
            print(stack[len(stack)-1])