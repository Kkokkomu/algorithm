# 0927
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph=[list(map(int,input().split())) for _ in range(N)]

si=sj=-1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            si = i
            sj = j
            break
    if sj != -1:
        break

wei = 2
wei_cnt = 0

di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs():
    global si, sj, wei, N

    fishs = []

    visited = [[-1] * N for _ in range(N)]
    visited[si][sj] = 0
    q = deque([(si,sj)])

    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni = ci + di[i]
            nj = cj + dj[i]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == -1 and graph[ni][nj] <= wei:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni,nj))
                if 0 < graph[ni][nj] < wei:
                    fishs.append((visited[ni][nj], (ni,nj)))
    
    return fishs


def eat():
    global N, si, sj, wei
    fishs = bfs()
    f_len = len(fishs)

    if f_len == 0:
        return -1
    elif f_len != 1:
        fishs.sort()

    return fishs[0]


res = 0
fish = eat()
while fish != -1:
    fi = fish[1][0]
    fj = fish[1][1]

    graph[fi][fj] = 9

    graph[si][sj] = 0
    si = fi
    sj = fj

    res += fish[0]

    wei_cnt += 1
    if wei_cnt == wei:
        wei += 1
        wei_cnt = 0

    fish = eat()

print(res)