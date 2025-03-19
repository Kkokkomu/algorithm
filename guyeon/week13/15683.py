# 320
import sys

input = sys.stdin.readline

N,M=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

di = [0,1,0,-1]
dj = [1,0,-1,0]

n1111 = [0,0,0,1]
n2222 = [1,0,1,0]
n3333 = [0,0,1,1]
n4444 = [1,1,1,0]
n5555 = [1,1,1,1]
dir = [0,n1111,n2222,n3333,n4444,n5555]

# i 좌표, j 좌표, cctv 종류, cctv 방향
cctvs = []
for i in range(N):
    for j in range(M):
        if graph[i][j]!=0 and graph[i][j]!=6:
            cctvs.append([i,j,graph[i][j],0])

simul = [g[:] for g in graph]
def cal(simul):
    res = 0
    for s in simul:
        res += s.count(0)
    return res

def go(si, sj, d,simul):
    while True:
        si += di[d]
        sj += dj[d]
        if 0<=si<N and 0<=sj<M:
            if simul[si][sj] == 6:
                break
            elif simul[si][sj] == '#' or 1<= simul[si][sj] <=6:
                continue
            else:
                simul[si][sj] = '#'
        else:
            break
def pt(simul):
    for s in simul:
        print(s)
def spread():
    simul = [g[:] for g in graph]
    for cctv in cctvs:
        for i in range(4):
            if dir[cctv[2]][(cctv[3]+i)%4] == 1:
                go(cctv[0], cctv[1], i, simul)
    # pt(simul)
    # print(cal(simul))
    return cal(simul)

res = 9999
lcctv = len(cctvs)
def playCCTV(idx):
    global res
    if idx == lcctv:
        res = min(spread(), res)
        return
    
    for i in range(4):
        cctvs[idx][3] = (cctvs[idx][3] + i)%4
        playCCTV(idx+1)
playCCTV(0)
print(res)