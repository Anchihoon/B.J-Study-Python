#BAEKJOON 10814
#나이수가 한자리로 들어오는 경우도 고려해야됨
import sys

R = []
n = int(sys.stdin.readline())
for i in range(n):
    a, n = sys.stdin.readline().split()
    R.append((int(a), n))

#sort()는 stable sort이다.
R.sort(key = lambda x : x[0])

for i in R:
    print(*i)