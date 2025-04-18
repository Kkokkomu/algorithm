#0836
import sys

input = sys.stdin.readline

C, R = map(int,input().split())
tg = int(input())

if C*R < tg:
    print(0)
    exit()

di = [1,0,-1,0]
dj = [0,1,0,-1]

graph = [[0] * C for _ in range(R)]

x=y=dir=0
graph[0][0] = 1

for n in range(1,C*R+1):
    if n == tg:
        print(y+1,x+1)
        break
    graph[x][y] = n

    nx = x+di[dir]
    ny = y+dj[dir]
    if not(0<=nx<R and 0<=ny<C and graph[nx][ny]==0):
        dir = (dir+1)%4
        nx = x+di[dir]
        ny = y+dj[dir]
    x = nx
    y = ny
# print(graph)