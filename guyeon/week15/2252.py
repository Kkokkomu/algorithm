#0412
import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indg = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    indg[b] += 1
    graph[a].append(b)

def topology():
    q = deque()
    res = []

    for i in range(1, len(indg)):
        if indg[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        res.append(now)

        for g in graph[now]:
            indg[g] -= 1
            if indg[g] == 0:
                q.append(g)
    
    return res

print(*topology(), sep=' ')