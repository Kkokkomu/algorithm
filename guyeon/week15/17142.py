# 14 28
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
virus = []
for i in range(N):
    ll =list(map(int,input().split()))
    for j in range(N):
        if ll[j] == 2:
            virus.append((i,j))
            ll[j] = 0
        elif ll[j] == 1:
            ll[j] = '-'
        elif ll[j] == 0:
            ll[j] = -1
    graph.append(ll)

acts = list(combinations(virus,M))

def pt(g):
    for gg in g:
        print(gg)
# pt(graph)
def ck(simul):
    global N
    # print("ch@@@@@@@@@@@@@@")
    # pt(simul)
    res = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == -1 and simul[i][j] == -1:
                return -1
            if simul[i][j] != '-' and graph[i][j] != 0 and res < simul[i][j]:
                res = simul[i][j]
    # print(res)
    # print()
    return res

di = [0,1,0,-1]
dj = [1,0,-1,0]
def spread(virus):
    global N
    # print()
    # print(virus)

    simul = []
    for i in range(N):
        simul.append(graph[i][:])
    # pt(simul)
    q = deque()

    for v in virus:
        q.append(v)
    
    while q:
        si,sj = q.popleft()
        # print(f"si: {si}, sj:{sj}")
        # pt(simul)

        for i in range(4):
            ni = si + di[i]
            nj = sj + dj[i]
            if 0<=ni<N and 0<=nj<N and \
                (simul[ni][nj] == -1 or simul[ni][nj] == 0):
                # print(f"ni:{ni},nj :{nj}")
                q.append((ni,nj))
                simul[ni][nj] = simul[si][sj] + 1
    
    # pt(simul)
    # print(ck(simul))
    return ck(simul)

res = sys.maxsize
for act in acts:
    s = spread(act)
    if s != -1 and res > s:
        res = s
if res == sys.maxsize:
    print(-1)
else:
    print(res)