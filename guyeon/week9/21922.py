# 1800
import sys

sys.setrecursionlimit(10**6)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

input = sys.stdin.readline

H, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[False] * M for _ in range(H)]
def prtV():
    for g in visited:
        print(g)
    print()

def prtG():
    for g in graph:
        print(g)
    print()
# prtG()

def go(d, i, j):
    if 0<=i<H and 0<=j<M:
        visited[i][j] = True
    else:
        return
    # prtV()
    if (graph[i][j] == 1 and (d == 2 or d == 0)) or (graph[i][j] == 2 and (d == 1 or d == 3)):
        return
    elif graph[i][j] == 3:
        if d == 0:
            go(3, i+di[3], j+dj[3])
        elif d == 1:
            go(2, i+di[2], j+dj[2])
        elif d == 2:
            go(1, i+di[1], j+dj[1])
        elif d == 3:
            go(0, i+di[0], j+dj[0])
    elif graph[i][j] == 4:
        if d == 0:
            go(1, i+di[1], j+dj[1])
        elif d == 1:
            go(0, i+di[0], j+dj[0])
        elif d == 2:
            go(3, i+di[3], j+dj[3])
        elif d == 3:
            go(2, i+di[2], j+dj[2])
    elif graph[i][j] == 9:
        return
    else:
        go(d, i+di[d], j+dj[d])

for i in range(H):
    for j in range(M):
        if graph[i][j] == 9:
            visited[i][j] = True
            for k in range(4):
                go(k, i+di[k], j+dj[k])

res=0
for g in visited:
    res += g.count(True)
print(res)