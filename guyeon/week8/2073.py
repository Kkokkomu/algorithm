import sys

input = sys.stdin.readline

D, P = map(int, input().split())

dp = [0] * (D+1)
dp[0] = 1e9

for _ in range(P):
    l, c = map(int, input().split())
    tmp = dp[:]
    for i in range(l,D+1):
        dp[i] = max(dp[i], min(c, tmp[i-l]))
print(dp[D])