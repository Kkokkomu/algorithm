import heapq
import sys

input = sys.stdin.readline

V,E = map(int,input().split())

start = int(input())

li = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    li[a].append((b,c))

INF = sys.maxsize
dijkstra = [INF] * (V+1)
dijkstra[start] = 0

pq = []
heapq.heappush(pq, (0,start))

while pq:
    wei, now = heapq.heappop(pq)

    if wei > dijkstra[now]:
        continue

    for next, nextwei in li[now]:
        cost = wei + nextwei
        if cost < dijkstra[next]:
            dijkstra[next] = cost
            heapq.heappush(pq, (cost, next))

for d in dijkstra[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)