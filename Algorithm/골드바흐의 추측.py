#BAEKJOON 6588
import sys
input = sys.stdin.readline

Prime = [False, False] + [True] * 999999

#에라토스테네스의 체를 통해 소수일때 True인 배열생성
for i in range(2, int(len(Prime) ** 0.5) + 1) :
    if Prime[i]:
        for j in range(i*2, 1000001, i):
            Prime[j] = False

while True :
    n = int(input())
    if n == 0:
        break
   
    for i in range(n-3,2,-2):
        if Prime[i] and Prime[n-i]:
            print(n,'=',n-i,'+',i)
            break
    
    else:
        print('Goldbach\'s conjecture is wrong.')