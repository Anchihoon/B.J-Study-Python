X = input()
X = int(X)
N = input()
N = int(N)
sum = 0
for i in range (0, N):
    p, c = input().split()
    p = int(p)
    c = int(c)
    sum = sum + (p * c)
if X == sum:
    print('Yes')
else :
    print('No')