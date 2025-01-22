# 16:45
import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(R)]
# print(graph)

# 먼저 물이 범람하는 함수 하나 만들기
# 그 다음 이동하면서 시간을 기록

def flow(sy, sx):
    queue = deque([(sy,sx)])

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C:
                if graph[ny][nx] == '.' or (type(graph[ny][nx]) == int and graph[ny][nx] < graph[y][x]-1):
                    graph[ny][nx] = graph[y][x] -1
                    queue.append((ny,nx))

def move(sy, sx):

    queue = deque([(sy,sx)])

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C:
                # print(graph[y][x])
                if graph[ny][nx] == '.' or (type(graph[ny][nx]) == int and graph[ny][nx] < graph[y][x]*(-1)-2):
                    graph[ny][nx] = graph[y][x] +1
                    queue.append((ny,nx))
                elif graph[ny][nx] == 'D':
                    return graph[y][x]+1
    return -1

# 범람 함수 먼저
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            graph[i][j] = -1
            flow(i, j)

# for g in graph:
#     print(g)

# S 찾기
sx, sy = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            graph[i][j] = 0
            res = move(i,j)
            if res == -1:
                print("KAKTUS")
            else:
                print(res)

# print(f"sy {sy}, sx {sx}")

