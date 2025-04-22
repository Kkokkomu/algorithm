#1134 ~ 1228
import sys

input = sys.stdin.readline

R,C,T = map(int,input().split())

graph = []
for i in range(R):
    li = list(map(int,input().split()))
    graph.append(li)

up = down = -1    
for i in range(R):
    if graph[i][0] == -1:
        up = i
        down = i+1
        break

def getDust():
    global R,C

    res = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                res.append(((i,j),graph[i][j]))
    return res

di = [0,1,0,-1]
dj = [1,0,-1,0]
def spread(dusts):
    global R,C

    for dust in dusts:
        si = dust[0][0]
        sj = dust[0][1]
        tic = dust[1]//5
        cnt = 0
        for i in range(4):
            ni = si + di[i]
            nj = sj + dj[i]
            if 0<=ni<R and 0<=nj<C and \
                graph[ni][nj] != -1:

                cnt += 1
                graph[ni][nj] += tic
                
        graph[si][sj] -= (tic * cnt)

def clean_up():
    global up

    for i in range(up-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(C-1):
        graph[0][i] = graph[0][i+1]
    for i in range(up):
        graph[i][C-1] = graph[i+1][C-1]
    for i in range(C-1, 1, -1):
        graph[up][i] = graph[up][i-1]
    graph[up][1] = 0

def clean_down():
    global down

    for i in range(down+1,R-1):
        graph[i][0] = graph[i+1][0]
    for i in range(C-1):
        graph[R-1][i] = graph[R-1][i+1]
    for i in range(R-1, down, -1):
        graph[i][C-1] = graph[i-1][C-1]
    for i in range(C-1, 1, -1):
        graph[down][i] = graph[down][i-1]
    graph[down][1] = 0

def clean():
    clean_up()
    clean_down()

def cnt_dust():
    res = 0
    for g in graph:
        for gg in g:
            if gg > 0:
                res += gg
    return res

for i in range(T):
    dusts = getDust()
    spread(dusts)
    clean()

print(cnt_dust())