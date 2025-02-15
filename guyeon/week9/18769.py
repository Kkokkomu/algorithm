import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    af = find(a)
    bf = find(b)

    if af == bf:
        return False
    elif af < bf:
        parent[af] = bf
    elif af > bf:
        parent[bf] = af
    
    return True

T = int(input())

for _ in range(T):
    R, C = map(int, input().split())

    edges = []
    for i in range(R):
        li = list(map(int, input().split()))
        for j in range(C-1):
            now = i*C + j
            edges.append((li[j], now, now+1))
    for i in range(R-1):
        li = list(map(int, input().split()))
        for j in range(C):
            now = i*C + j
            edges.append((li[j], now, now+C))
    
    parent=[]
    for i in range(R):
        for j in range(C):
            parent.append(i*C + j)
            
    edges.sort()
    res = 0
    for m, a, c in edges:
        if union(a,c):
            res += m
    print(res)