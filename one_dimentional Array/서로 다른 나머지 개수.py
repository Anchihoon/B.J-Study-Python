#BAEKJOON 3052
S = []
for i in range(10):
    n = int(input()) % 42
    if n not in S:
        S.append(n) 
print(len(S))