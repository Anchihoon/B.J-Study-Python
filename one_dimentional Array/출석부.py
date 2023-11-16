#BAEKJOON 5597
A = []
for i in range(30):
    A.append(0)
for i in range(28):
    s = int(input())
    A[s-1] = 1
for i in range(30):
    if A[i] == 0:
        print(i+1)