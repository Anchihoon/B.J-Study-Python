#BAEKJOON 2439
N = int(input())
k = 1
for i in range(0,N):
    for l in range(N-k,0,-1):
        print(' ',end='')
    for j in range(k):
        print('*',sep='',end='')
    k = k + 1
    print()    