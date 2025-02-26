#900
import sys

input = sys.stdin.readline

N,M = map(int, input().split())

INF = sys.maxsize

graph = list(map(int, input().split()))
dp=[]
dp.append([INF, graph[0],graph[0]])
for i in range(1,M-1):
    dp.append([graph[i],graph[i],graph[i]])
dp.append([graph[-1],graph[-1],INF])

for _ in range(1, N):
    graph = list(map(int, input().split()))
    # print(f"graph: {graph}")
    tmp = []

    tmp.append([INF,dp[0][2]+graph[0], min(dp[1][1],dp[1][0])+graph[0]])
    for i in range(1,M-1):
        tmp.append([min(dp[i-1][1],dp[i-1][2])+graph[i], min(dp[i][0],dp[i][2])+graph[i], min(dp[i+1][0],dp[i+1][1])+graph[i]])
    tmp.append([min(dp[-2][1], dp[-2][2])+graph[-1], dp[-1][0]+graph[-1], INF])

    dp = tmp
    # print(f"dp: {dp}")

mmn=INF
for d in dp:
    mn = min(d)
    if mn < mmn:
        mmn = mn
print(mmn)