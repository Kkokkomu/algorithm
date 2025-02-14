import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())

graph_go = [[]for _ in range(N+1)]
graph_rt = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph_go[a].append((b,c))
    graph_rt[b].append((a,c))

def dijkstra(start, graph):
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0,start))

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for near in graph[now]:
            if distance[near[0]] > dist + near[1]:
                distance[near[0]] = dist + near[1]
                heapq.heappush(pq, (distance[near[0]], near[0]))

distance = [INF] * (N+1)
dijkstra(X, graph_go)
tmp = distance

distance = [INF] * (N+1)
dijkstra(X, graph_rt)

res = 0
for i in range(1, N+1):
    if res < tmp[i] + distance[i]:
        res = tmp[i] + distance[i]
print(res)