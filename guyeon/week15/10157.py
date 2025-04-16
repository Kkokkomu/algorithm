#0836
import sys

input = sys.stdin.readline

C, R = map(int,input().split())
tg = int(input())

di = [1,0,-1,0]
dj = [0,1,0,-1]

graph = [[0] * C for _ in range(R)]

x=y=0
n=1
dir = 0
graph[0][0] = 1
if n == tg:
    print(y+1,end=' ')
    print(x+1)
    exit()

while True:
    ni = x+di[dir]
    nj = y+dj[dir]

    if 0<=ni<R and 0<=nj<C and graph[ni][nj]==0:
        x=ni
        y=nj
        n+=1
        graph[x][y] = n
        if n == tg:
            print(y+1,end=' ')
            print(x+1)
            break
    else:
        dir = (dir+1)%4
        ni = x+di[dir]
        nj = y+dj[dir]
        if not(0<=ni<R and 0<=nj<C) or graph[ni][nj] != 0:
            print(0)
            break

# print(graph)