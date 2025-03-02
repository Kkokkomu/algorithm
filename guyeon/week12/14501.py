#0657 ~ 0714
import sys

input = sys.stdin.readline

N=int(input())
days = [[-1,-1]]
for _ in range(N):
    days.append(list(map(int,input().split())))

def dfs(day, ssum): # 백트레킹
    if day == N+1:
        return ssum
    if day <= N: # 아직 마지막 날이 아니라면, 오늘 상담을 하는 경우와 안하는 경우 둘 다 호출해봄
        return max(dfs(day + days[day][0], ssum+days[day][1]), dfs(day + 1, ssum))
    return -1

print(dfs(1, 0))