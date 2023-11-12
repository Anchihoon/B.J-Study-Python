h, m = input().split()
h = int(h)
m = int(m)
m = m - 45
if m < 0 :
    m = 60 + m
    if h == 0:
        h = 23
    else :
        h = h - 1
print(h, m)