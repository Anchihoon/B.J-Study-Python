#BAEKJOON 24313
a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())
fn = a1 * n0 + a0
gn = c * n0

if fn > gn or a1 > c:
    print('0')
else :
    print('1')