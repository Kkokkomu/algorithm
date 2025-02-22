# 854
import sys
import heapq

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    af = find(a)
    bf = find(b)

    if af == bf:
        return False
    if af < bf:
        parent[af] = bf
    else:
        parent[bf] = af
    return True

N, M = map(int, input().split())

parent=[i for i in range(N+1)]

pq = []
for _ in range(M):
    a,b,m = map(int, input().split())
    heapq.heappush(pq, (m,a,b))

cnt = 0
res = 0
while pq:
    if cnt >= N-2:
            print(res)
            exit()
    m,a,b = heapq.heappop(pq)
    if union(a,b):
        res += m
        cnt += 1
        