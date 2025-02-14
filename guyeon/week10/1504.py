# 1 => v1 => v2 => N

# 1 => v2 => v1 => N

# 두 개 고려 했어야함

# 다익스트라 실행할 때마다 distance 배열 초기화 했어야함
import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())

graph=[[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start):
    distance[start] = 0

    pq =[]
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for near in graph[now]:
            if dist + near[1] < distance[near[0]]:
                distance[near[0]] = dist + near[1]
                heapq.heappush(pq, (distance[near[0]], near[0]))

v1, v2 = map(int, input().split())

distance = [INF] * (N+1)
dijkstra(v1)
if distance[1] == INF or distance[v2] == INF:
    print(-1)
    exit()
a = distance[1] 
b = distance[v2]
c = distance[N]

distance = [INF] * (N+1)
dijkstra(v2)
if distance[N] == INF:
    print(-1)
    exit()
d = distance[1]
e = distance[N]

print(b + min((d+c), (a+e)))