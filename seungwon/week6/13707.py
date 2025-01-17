# pypy로 풀어야 시간초과가 나지 않음

N, K = map(int, input().split())
# dp[a][b] = a를 b개의 수로 나타내는 방법의 수
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 초기값 설정
for i in range(N + 1):
    dp[i][1] = 1
for j in range(1, K + 1):
    dp[0][j] = 1

# dp[a][b] = dp[a - 1][b] + dp[a][b - 1]
for a in range(1, N + 1):
    for b in range(2, K + 1):
        dp[a][b] = (dp[a - 1][b] + dp[a][b - 1]) % 1000000000

print(dp[N][K])
