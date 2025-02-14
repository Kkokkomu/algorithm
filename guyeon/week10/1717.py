import sys

input = sys.stdin.readline

N, M = map(int, input().split())

parent = []
for i in range(N+1):
    parent.append(i)

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    a=find(a)
    b=find(b)

    if a<b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(M):
    a,b,c = map(int, input().split())

    if a==0:
        union(b,c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")