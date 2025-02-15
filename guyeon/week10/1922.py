import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    af = find(a)
    bf = find(b)

    if af==bf:
        return False
    elif af < bf:
        parent[af] = bf
    elif af > bf:
        parent[bf] = af

    return True

edges = []
for _ in range(M):
    a,b,c = map(int, input().split())
    if a!=b:
        edges.append((c,a,b))

parent = [i for i in range(N+1)]

edges.sort()
res = 0
for m, a, b in edges:
    if union(a,b):
        res += m
        
print(res)