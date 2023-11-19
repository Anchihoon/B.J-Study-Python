#BAEKJOON 2444
N = int(input())
k = 1
l = 1
for i in range(N):
    for j in range(N-l,0,-1):
        print(' ',end='')
    for j in range(k):
        print('*',sep='',end='')
    print()
    l = l + 1
    k = k + 2
for i in range(N-1):
    for j in range(l-1,N+1):
        print(' ',end='')
    for j in range(k-4):
        print('*',sep='',end='')
    print()
    k = k - 2
    l = l - 1