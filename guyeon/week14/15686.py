# 1738
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

N,M = map(int,input().split())

huss = []
cks = []
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(N):
        if row[j] == 2:
            cks.append((i,j))
        elif row[j] == 1:
            huss.append((i,j))

def uc(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def ckdist(hus):
    res = 9999
    for i in range(len(cks)):
        if visited[i]:
            uu = uc(cks[i],hus)
            if res > uu:
                res = uu
    return res

def ckdistall():
    res = 0
    for hus in huss:
        res += ckdist(hus)
    return res

res = 9999
visited = [False] * len(cks)
def dfs(idx, cnt):
    global res
    if cnt == M:
        cc = ckdistall()
        if res > cc:
            res = cc
        return
    for i in range(idx, len(cks)):
        if not visited[i]:
            visited[i] = True
            dfs(idx+1, cnt+1)
            visited[i] = False
    return res

print(dfs(0,0))