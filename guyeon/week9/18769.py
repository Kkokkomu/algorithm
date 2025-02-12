import sys
from collections import defaultdict

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
r, c = -1, -1
graph = None

parent = []
q = []

def find(p):
    global parent

    if parent[p] == p:
        return p
    parent[p] = find(parent[p])
    return parent[p]

def kruskal():
    global parent, q
    parent = [x for x in range(r * c)]

    cnt = 0
    total = 0
    size = len(q)
    q.sort()

    for i in range(size):
        w, a, b = q[i]

        pa = find(a)
        pb = find(b)

        if pa == pb:
            continue

        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

        cnt += 1
        total += w

        if cnt == r * c - 1:
            return total

    return total

for _ in range(T):
    r, c = tuple(map(int, input().split()))
    graph = defaultdict(list)
    q = []

    # 그래프 구축
    for i in range(r):
        w = list(map(int, input().split()))
        for j in range(c - 1):
            cur = i * c + j
            next = cur + 1
            q.append((w[j], cur, next))

    for i in range(r - 1):
        w = list(map(int, input().split()))
        for j in range(c):
            cur = i * c + j
            next = cur + c
            q.append((w[j], cur, next))

    print(kruskal())