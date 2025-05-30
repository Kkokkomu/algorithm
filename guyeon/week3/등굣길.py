def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles] 
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    
    # print(dp)
    
    dp[1][1]=1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            
#     print(dp)
    
    return dp[n][m]