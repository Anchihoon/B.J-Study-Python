#BAEKJOON 10799
#'('를 만나면 무조건 push
#')'를 만나면 전에 '('면 레이저니까 스택에 있는 '(' 개수많큼 cnt증가
#')'만나고 전에 '('가 아니면 통나무가 끝났으니까 1추가
import sys

P = list(sys.stdin.readline().strip())
stack = []
cnt = 0
stack.append(P[0])
for i in range(1,len(P)):
    if P[i] == '(':
        stack.append(i)
    else : 
        if P[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        else :
            stack.pop()
            cnt += 1
print(cnt)