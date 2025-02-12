#0135
import sys
import heapq

input = sys.stdin.readline

N,M,X,Y = map(int, input().split())
# 집 개수, 간선 개수, 최대거리, 성현의 집

graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = sys.maxsize
distance = [INF] * N
distance[Y] = 0 # 시작지점은 0

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        # print(pq)
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for near in graph[now]:
            if dist + near[1] < distance[near[0]]:
                distance[near[0]] = dist + near[1]
                heapq.heappush(pq, (distance[near[0]], near[0]))

dijkstra(Y)


distance.sort()
if X< distance[-1]:
    print(-1)
    exit()

res = 0
tmp = 0
for i in range(1, N):
    # print(i)
    if tmp + distance[i]*2 <= X:
        tmp += distance[i]*2
    else:
        # print(f"tmp : {tmp}")

        tmp =distance[i]*2
        res +=1
print(res +(1 if tmp > 0 else 0))
