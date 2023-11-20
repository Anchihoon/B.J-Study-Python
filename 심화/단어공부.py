#BAEKJOON 1157

N = input().upper()
unique_N = list(set(N))
A = []
for i in unique_N:
    c = N.count(i)
    A.append(c)
if A.count(max(A)) != 1:
    print('?')
else :
    print(unique_N[A.index(max(A))])