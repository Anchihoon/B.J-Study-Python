#BAEKJOON 17413
import sys

S = sys.stdin.readline()
state = False # 괄호안에 있으면 True
stack = [] # 괄호밖일 때 활요할 스택
for i in S:
    if i == '<':
        state = True
        while stack != []:
            print(stack.pop(),sep='',end='')
    stack.append(i)
    
    if i == '>':
        state = False
        while stack != []:
            print(stack[0],sep='',end='')
            del stack[0]

    if (i == ' ' or i == '\n') and state == False:
        stack.pop()
        while stack != []:
            print(stack.pop(),sep='',end='')
        print(' ',end='')