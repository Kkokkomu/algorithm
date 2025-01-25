import sys

n = int(sys.stdin.readline())

glasses = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(n)]

if n==1:
    print(glasses[0])
    exit()
if n==2:
    print(glasses[0]+glasses[1])
    exit()
if n==2:
    print(max(glasses[0]+glasses[1],glasses[0]+glasses[2],glasses[1]+glasses[2]))
    exit()

dp[0] = glasses[0]
dp[1] = glasses[0] + glasses[1]
dp[2] = max(glasses[0]+glasses[1],glasses[0]+glasses[2],glasses[1]+glasses[2])

for i in range(3,n):
    dp[i] = max(dp[i-3]+glasses[i-1]+glasses[i], dp[i-2]+glasses[i], dp[i-1])
print(dp)
print(dp[n-1])