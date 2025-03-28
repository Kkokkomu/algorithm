# 1935 ~ 1948 58~10
import sys

input = sys.stdin.readline

R,C,N = map(int,input().split())

graph = []
for i in range(R):
    e = list(input().rstrip())
    for j in range(C):
        if e[j] == '.':
            e[j] = 0
        else:
            e[j] = 2
    graph.append(e)

time = 1

di = [0,1,0,-1]
dj = [1,0,-1,0]
def boom(si, sj):
    graph[si][sj] = 0
    for i in range(4):
        ni = si+di[i]
        nj = sj+dj[i]
        if 0<=ni<R and 0<=nj<C:
            graph[ni][nj] = 0

def boomAll(boomList):
    for bl in boomList:
        boom(bl[0], bl[1])

while time < N:
    time += 1

    boomList = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 3:
                boomList.append((i,j))
            else:
                graph[i][j] +=1
    boomAll(boomList)

for i in range(R):
    for j in range(C):
        if graph[i][j] == 0:
            graph[i][j] = '.'
        else:
            graph[i][j] = 'O'
    print("".join(graph[i]))
    