#0657
import sys

input = sys.stdin.readline

N=int(input())
days = [[-1,-1]]
for _ in range(N):
    days.append(list(map(int,input().split())))

# print(days)

def dfs(day, ssum):
    # print()
    # print(f"day : {day}, ssum : {ssum}")
    if day == N+1:
        # print(f"return! ssum : {ssum}")
        return ssum
    if day <= N:
        return max(dfs(day + days[day][0], ssum+days[day][1]), dfs(day + 1, ssum))
    return -1

print(dfs(1, 0))