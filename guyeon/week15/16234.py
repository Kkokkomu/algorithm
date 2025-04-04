# 1747
import sys
from collections import deque

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

di = [0,1,0,-1]
dj = [1,0,-1,0]

def dfs(si, sj, visited):
    global N

    q = deque([(si,sj)])

    group = [(si,sj)]
    pps = graph[si][sj]
    while q:
        si,sj = q.popleft()
        visited[si][sj] = True

        for i in range(4):
            ni = si + di[i]
            nj = sj + dj[i]
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] == False:
                    if L <= abs(graph[si][sj]-graph[ni][nj]) <= R:
                        visited[ni][nj] = True
                        pps += graph[ni][nj]
                        group.append((ni,nj))
                        q.append((ni,nj))
    
    if len(group) != 1:
        p = pps//len(group)
        for i,j in group:
            graph[i][j] = p
    else:
        return True

res = 0
while res < 2000:
    res += 1
    visited = [[False] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                if dfs(i,j,visited):
                    tmp += 1
    if tmp == N*N:
        res -=1
        break

print(res)