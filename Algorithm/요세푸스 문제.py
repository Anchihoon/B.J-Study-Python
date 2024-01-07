#BAEKJOON 1158
import sys

N, K = map(int, sys.stdin.readline().split())
J = list(range(1, N+1))

R = []
turn = 0

while J:
    '''
    if turn % K == 0:
        turn = 0
        R.append(J.pop(i))
    i += 1
    turn += 1
    if i == len(J):
        i = 0
    '''
    turn = (turn + K - 1) % len(J)
    R.append(J.pop(turn))
print('<',end='')
print(*R, sep=', ',end='')
print('>')