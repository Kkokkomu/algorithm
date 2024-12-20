def solution(N, number):
    # dp[i] = N을 i번 사용해서 만들 수 있는 수의 집합
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # N을 i번 이어붙인 수
        dp[i].add(int(str(N) * i))

        # N을 i번 사용해서 만들 수 있는 수의 집합을 만들기 위해
        # j를 1부터 i-1까지 돌면서 dp[j]와 dp[i-j]의 원소들을 모두 고려
        # ex) i가 5일 때, j가 1, 2, 3, 4일 때의 경우를 모두 고려 (dp[1] + dp[4], dp[2] + dp[3], dp[3] + dp[2], dp[4] + dp[1])
        for j in range(1, i):
            for e in dp[j]:
                for e2 in dp[i - j]:
                    dp[i].add(e + e2)
                    dp[i].add(e - e2)
                    dp[i].add(e * e2)
                    if e2 != 0:
                        dp[i].add(int(e / e2))

        # number가 dp[i]에 있으면 i를 반환
        if number in dp[i]:
            return i

    # 8번 반복했는데도 number가 없으면 -1 반환
    return -1
