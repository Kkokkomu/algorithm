#0925
import sys
from collections import deque

input = sys.stdin.readline

di = [0,1,0,-1]
dj = [1,0,-1,0]

N,M = map(int,input().split())
def pgraph():
    for g in graph:
        print(g)

graph = [list(map(int, input().split())) for _ in range(N)]
# pgraph()

virs = []
halls = []
wall = 3
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virs.append((i,j))
        elif graph[i][j] == 0:
            halls.append((i,j))
        else:
            wall+=1
# print(wall)
# print(halls)
def spread():
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    # print()
    # pgraph()
    for vir in virs:
        q = deque([vir])
        cnt+=1

        while q:
            virI, virJ = q.popleft()
            for i in range(4):
                ni = virI + di[i]
                nj = virJ + dj[i]
                if 0<=ni<N and 0<=nj<M and visited[ni][nj] == False and graph[ni][nj] == 0:
                    cnt+=1
                    visited[ni][nj] = True
                    q.append((ni,nj))
    # print(N*M - cnt - wall)
    return N*M - cnt - wall

res = 0
lenW = len(halls)
for i in range(lenW):
    for j in range(i+1, lenW):
        for k in range(j+1, lenW):
            graph[halls[i][0]][halls[i][1]] = 1
            graph[halls[j][0]][halls[j][1]] = 1
            graph[halls[k][0]][halls[k][1]] = 1
            res = max(res, spread())
            graph[halls[i][0]][halls[i][1]] = 0
            graph[halls[j][0]][halls[j][1]] = 0
            graph[halls[k][0]][halls[k][1]] = 0

print(res)