#BAEKJOON 2745

NUM = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = input().split()
B = int(B)
sum = 0

for i in range(len(N),0,-1):
    a = NUM.index(N[i-1]) 
    sum = sum + a * B**(len(N)-i)

print(sum)