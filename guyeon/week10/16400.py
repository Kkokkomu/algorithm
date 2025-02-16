# 일단 소수 구하고
# 최대한 큰 소수부터 순회
    # 해당수*2 부터 빼면서 상대 차수에 해당하는 만큼 더해주기
import sys

N = int(sys.stdin.readline())

prime = [True] * (N+1)

for i in range(2, int(N**(1/2))+1):
    for j in range(i+i, N+1, i):
        prime[j] = False

dp = [0] * (N+1)
for i in range(N, 1, -1):
    if prime[i]:
        dp[i] = 1
        for j in range(i+i, N+1):
            if j-i != 0:
                dp[j] = (dp[j] + dp[j-i])%123456789

print(dp[N])