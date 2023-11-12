H, M = input().split()
m = input()
H = int(H)
M = int(M)
m = int(m)
M = M + m
H = H + (M//60)
M = M % 60
if H >= 24 :
    H = H - 24
print(H, M)