#1242
import sys
from collections import deque

input = sys.stdin.readline

N,M,K = map(int,input().split())

addList = []
for _ in range(N):
    addList.append(list(map(int,input().split())))

trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)

for i in range(N):
    for j in range(N):
        if trees[i][j]:
            tl = list(trees[i][j])
            tl.sort()
            trees[i][j] = deque(tl)

graph = [[5]*N for _ in range(N)]

def spring():
    res = []
    for r in range(N):
        for c in range(N):
            len_ = len(trees[r][c])
            for i in range(len_):
                v = trees[r][c]
                if graph[r][c] >= v[i]: # 만약 양분이 아직 있다면
                    graph[r][c] -= v[i]
                    trees[r][c][i] += 1
                else: # 양분이 충분하지 않다면 그 나무부터 뒤의 나무들은 전부 죽음처리
                    for _ in range(len(v) - i):
                        res.append((r,c,trees[r][c].pop()))
                    break
    return res

def summer(deads):
    for dead in deads:
        graph[dead[0]][dead[1]] += dead[2]//2

di = [0,1,1,1,0,-1,-1,-1]
dj = [1,1,0,-1,-1,-1,0,1]
def autc():
    ad = []
    for r in range(N):
        for c in range(N):
            len_ = len(trees[r][c])
            for i in range(len_):
                v = trees[r][c]
                if v[i]%5 == 0:
                    for j in range(8):
                        nr = r + di[j]
                        nc = c + dj[j]
                        if 0<=nr<N and 0<=nc<N:
                            ad.append((nr,nc))
    for a in ad:
        trees[a[0]][a[1]].appendleft(1)

def winter():
    for i in range(N):
        for j in range(N):
            graph[i][j] += addList[i][j]

for i in range(K):
    deads = spring()
    summer(deads)
    autc()
    winter()

res = 0
for i in range(N):
    for j in range(N):
        res += len(trees[i][j])
print(res)