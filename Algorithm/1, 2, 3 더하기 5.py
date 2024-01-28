#BAEKJOON 15990
import sys
input = sys.stdin.readline

dp = [[0]*3 for _ in range(100001)]

n = int(input())
dp[1][0] = 1
dp[2][1] = 1
dp[3][2] = 1
dp[3][1] = 1
dp[3][0] = 1


for i in range(4,100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009
    
for _ in range(n):
    k = int(input())
    print(sum(dp[k]) % 1000000009)