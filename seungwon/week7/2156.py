n = int(input())
li = [int(input()) for _ in range(n)]
# dp[i] = (i-1번째 포도주를 마셨을 때 최대값, i-1번째 포도주를 마시지 않았을 때 최대값)
dp = [(0, 0)] * n

if n == 1:
    print(li[0])
else:
    dp[0] = (li[0], li[0])
    dp[1] = (li[0] + li[1], li[1])

    for i in range(2, n):
        dp[i] = (
            max(dp[i - 1][1] + li[i], dp[i - 1][0]),
            max(dp[i - 2][0], dp[i - 2][1]) + li[i],
        )

    print(max(dp[n - 1][0], dp[n - 1][1]))
