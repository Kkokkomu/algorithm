import sys
from collections import deque
# 1240

dj = [1,0,-1,0,1,-1,-1,1]
di = [0,1,0,-1,1,1,-1,-1]

def bfs(si, sj):
    queue = deque([(si,sj)])

    while queue:
        
        i, j = queue.popleft()

        for n in range(8):
            ni = i + di[n]
            nj = j + dj[n]
            if 0<=ni<H and 0<=nj<W :
                if graph[ni][nj] == 1:
                    queue.append((ni,nj))
                    graph[ni][nj] = -1

W, H = map(int, sys.stdin.readline().split())

while W!=0 and H!=0:
    res = 0

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                res+=1
                graph[i][j]=-1
                bfs(i,j)
    
    print(res)
    W, H = map(int, sys.stdin.readline().split())