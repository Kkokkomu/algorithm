from collections import deque
import sys
import heapq

input = sys.stdin.readline

start, tg = map(int, input().split())

li=[[] for _ in range(200001)]
li[0].append((1,1))
for i in range(1, 200000):
    if i*2 <= 200000:
        li[i].append((0,i*2))
    li[i].append((1,i-1))
    li[i].append((1,i+1))
li[200000].append((1,199999))

pq=[]
heapq.heappush(pq, (0,start))

INF = sys.maxsize
dij = [INF] * 200001
dij[start] = 0

while pq:
    wei, now = heapq.heappop(pq)

    if wei > dij[now]:
        continue

    for next_wei, next in li[now]:
        cost = next_wei + wei
        if cost < dij[next]:
            dij[next] = cost
            heapq.heappush(pq, (cost, next))

print(dij[tg])