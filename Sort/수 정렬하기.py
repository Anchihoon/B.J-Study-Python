#BAEKJOON 2750
#삽입정렬
N = int(input())
A = []
for i in range(N):
    n = int(input())
    A.append(n)
for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key
for i in range(len(A)):
    print(A[i])