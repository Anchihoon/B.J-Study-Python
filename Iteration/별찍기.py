#BAEKJOON 2438
N = int(input())
for i in range(1,N+1):
    for j in range(i):
        print('*',sep='',end='')
    print()
