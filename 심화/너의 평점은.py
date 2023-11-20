#BAEKJOON 25206
import sys

G = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
P = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
sum_p = 0
sum = 0
for i in range(20):
    N, p, g = sys.stdin.readline().split()
    if g != 'P':
        sum_p += float(p)
        sum += P[G.index(g)] * float(p)
print(sum / sum_p)       