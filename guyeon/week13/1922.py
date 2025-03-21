import sys

input = sys.stdin.readline

N=int(input())
M=int(input())

eg = []
for _ in range(M):
    a,b,c=map(int,input().split())
    if a!=b:
        eg.append((c,a,b))

eg.sort()

parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        if pa < pb:
            parent[pa] = parent[pb]
        else:
            parent[pb] = parent[pa]
        return True
    else:
        return False

res = 0
for w,a,b in eg:
    if union(a,b):
        res += w

print(res)