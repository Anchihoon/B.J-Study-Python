#BAEKJOON 2941
N = input()
A = ['c=','c-','dz=','d-','lj','nj','s=','z=']
i = 0
cnt = 0

while i < len(N):
    if i+1 < len(N) and N[i] + N[i+1] in A:
        cnt += 1
        i += 2
    elif i+2 < len(N) and N[i] + N[i+1] + N[i+2] in A:
        cnt += 1
        i += 3
    else :
        cnt += 1
        i += 1
print(cnt)