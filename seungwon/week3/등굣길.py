def solution(m, n, puddles):
    # dp[i][j] = (i, j)까지의 경로의 수
    dp = [[0] * (m + 2) for i in range(n + 1)]
    dp[1][1] = 1

    # 웅덩이가 있는 곳은 -1로 표시
    for li in puddles:
        if li:
            dp[li[1]][li[0]] = -1

    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 왼쪽, 위쪽의 경로 수를 더함
    # 단, 웅덩이가 있는 곳은 제외
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1 or (i == 1 and j == 1):
                continue
            # 위쪽과 왼쪽의 경로 수를 더함
            # 단, 웅덩이(-1)인 경우는 0으로 처리
            prev_top = dp[i - 1][j] if dp[i - 1][j] != -1 else 0
            prev_left = dp[i][j - 1] if dp[i][j - 1] != -1 else 0
            # 경로의 수를 1000000007로 나눈 나머지를 저장
            dp[i][j] = (prev_top + prev_left) % 1000000007

    return dp[n][m]
