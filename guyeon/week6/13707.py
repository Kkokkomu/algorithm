import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0]*(k+1) for _ in range(n+1)]

# 1개의 수로 i를 만드는 방법
for i in range(n+1):
    dp[i][1] = 1    

# j개의 수로 0을 만드는 경우
for j in range(1, k+1):
    dp[0][j] = 1

# 점화식 적용
for i in range(1, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % 1_000_000_000

print(dp[n][k])