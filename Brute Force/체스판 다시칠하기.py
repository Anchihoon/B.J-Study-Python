#BAEKJOON 1018
import sys

def White(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if A[i][j] != X[x+i][y+j]:
                cnt += 1
    return cnt

def Black(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if B[i][j] != X[x+i][y+j]:
                cnt += 1
    return cnt

A = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW']

B = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB']

X = []
stack = []
m, n = map(int,sys.stdin.readline().split())
for _ in range(m):
    X.append(sys.stdin.readline().strip())

for k in range(m-8+1):
    for l in range(n-8+1):
        stack.append(Black(k,l))
        stack.append(White(k,l))

print(min(stack))