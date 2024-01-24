#BAEKJOON 17103
#소수 판별 함수를 갈기고
#골드바흐를 입력수의 절반까지만 수행 하면됨 그럼 순서다른 경우 커버가능
import sys
input = sys.stdin.readline

Prime = [False, False] + [True] * 999999

#에라토스테네스의 체를 통해 소수일때 True인 배열생성
for i in range(2, 1000001):
    if Prime[i]:
        for j in range(i*2, 1000001, i):
            Prime[j] = False

n = int(input())

for i in range(n):
    k = int(input())
    cnt = 0
    for j in range(2, k//2+1):
        if Prime[j] and Prime[k-j]:
            cnt += 1
    print(cnt)   