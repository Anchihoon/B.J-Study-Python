#BAEKJOON 1874
import sys

#입력받기
n = int(sys.stdin.readline())
stack = []
ans = []
state = True
a = 1

#스택에 push 및 pop하면서 출력배열 생성
for i in range(n):
    c = int(sys.stdin.readline())
    while a <= c:
        stack.append(a)
        ans.append('+')
        a += 1
    if stack[len(stack)-1] == c:
        stack.pop()
        ans.append('-')
    else :
        state = False

#출력
if state == False:
    print('NO')
else :
    for i in range(len(ans)):
        print(ans[i])

         