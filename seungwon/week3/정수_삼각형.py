def solution(triangle):
    # dp[i][j] = i번째 줄 j번째 숫자까지의 최대합
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    # 초기값 설정
    dp[0][0] = triangle[0][0]

    # dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    for i, li in enumerate(triangle[1:], 1):
        # 각 줄의 숫자들에 대해
        for j, e in enumerate(li):
            # 왼쪽으로부터 합과 오른쪽으로부터 합을 구함
            sum_left = 0
            sum_right = 0
            # 왼쪽
            if j > 0:
                sum_left = e + dp[i - 1][j - 1]
            # 오른쪽
            if j != len(li) - 1:
                sum_right = e + dp[i - 1][j]
            # 둘 중 큰 값을 선택
            dp[i][j] = max(sum_left, sum_right)

    # 마지막 줄의 최대값을 반환
    return max(dp[-1])
