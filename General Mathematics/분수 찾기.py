#BAEKJOON 1193
n = int(input())
line = 1

while n > line:
    n -= line
    line += 1
        
if line % 2 == 1:
    a = line - n + 1
    b = n
else :
    a = n
    b = line - n + 1

print(a,'/',b,sep='')