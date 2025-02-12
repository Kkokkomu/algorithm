import sys
import heapq

imput = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

st, end = map(int, input().split())

INF = sys.maxsize
dist = [INF] * (N+1)
dist[st] = 0

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        # print(pq)
        distance, now = heapq.heappop(pq)

        if dist[now] < distance:
            continue

        for near in graph[now]:
            if distance + near[1] < dist[near[0]]:
                dist[near[0]] = distance + near[1]
                heapq.heappush(pq, (dist[near[0]], near[0]))

dijkstra(st)

print(dist[end])