#BAEKJOON 11653
n = int(input())
i = 2
A = []

while n != 1:
    if n % i == 0:
        A.append(i)
        n = n / i
        print(i)
    else :
        i = i + 1 