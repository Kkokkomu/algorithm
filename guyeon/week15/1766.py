# 0424
import sys
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indg = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    indg[b] += 1
    graph[a].append(b)

def topology():
    q = []
    res = []

    for i in range(1, len(indg)):
        if indg[i] == 0:
            heapq.heappush(q,i)
    
    while q:
        now = heapq.heappop(q)
        res.append(now)

        for g in graph[now]:
            indg[g] -= 1
            if indg[g] == 0:
                heapq.heappush(q,g)
    
    return res

print(*topology(), sep=' ')
