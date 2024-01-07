#BAEKJOON 1406
#remove 나 insert의 경우 O(n)의 시간복잡도때문에 제한시간을 초과
#O(1)인 append와 pop을 쓰기위해 스택 두개를 만듦
#마지막에 두 스택을 합치면 완성
import sys

st1 = list(sys.stdin.readline().strip())
st2 = []
n = int(sys.stdin.readline())

for i in range(n):
    w = list(sys.stdin.readline().split())
    if w[0] == 'P': 
        st1.append(w[1])
       
    elif w[0] == 'L':
        if st1:
            st2.append(st1.pop())
          
    elif w[0] == 'D':   
        if st2:
            st1.append(st2.pop())
       
    elif w[0] == 'B':
        if st1:
            st1.pop()

print(*st1,sep='',end='')
print(*st2[::-1],sep='')