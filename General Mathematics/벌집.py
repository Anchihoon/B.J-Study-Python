#BAEKJOON 2292
N = int(input())
i = 1
a = 1

while N > a :
    a = a + 6 * i
    i += 1
print(i)