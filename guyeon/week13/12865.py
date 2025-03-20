import sys

input = sys.stdin.readline
#319
N,K= map(int,input().split())

weight = [0] * (N+1)
value = [0] * (N+1)
for i in range(1,N+1):
    weight[i], value[i] = map(int,input().split())

dp = [[0] * (N+1) for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(1, N+1):
        if weight[j] <= i:
            dp[i][j] = max(dp[i-weight[j]][j-1]+value[j], dp[i][j-1])
        else:
            dp[i][j] = dp[i][j-1]

print(dp[K][N])