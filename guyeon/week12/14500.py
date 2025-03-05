#0552 ~ 0608 0636~
import sys

input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

tet = []
def makeTet():
    a1 = [[1,1,1,1]]
    tet.append(a1)
    a2 = [[1],[1],[1],[1]]
    tet.append(a2)

    b1 = [[1,1],[1,1]]
    tet.append(b1)

    c1 = [[1,0],[1,0],[1,1]]
    tet.append(c1)
    c2 = [[0,0,1],[1,1,1]]
    tet.append(c2)
    c3 = [[1,1],[0,1],[0,1]]
    tet.append(c3)
    c4 = [[1,1,1],[1,0,0]]
    tet.append(c4)
    c5 = [[0,1],[0,1],[1,1]]
    tet.append(c5)
    c6 = [[1,1,1],[0,0,1]]
    tet.append(c6)
    c7 = [[1,1],[1,0],[1,0]]
    tet.append(c7)
    c8 = [[1,0,0],[1,1,1]]
    tet.append(c8)

    d1 = [[1,0],[1,1],[0,1]]
    tet.append(d1)
    d2 = [[0,1,1],[1,1,0]]
    tet.append(d2)
    d3 = [[0,1],[1,1],[1,0]]
    tet.append(d3)
    d4 = [[1,1,0],[0,1,1]]
    tet.append(d4)

    e1 = [[1,1,1],[0,1,0]]
    tet.append(e1)
    e2 = [[1,0],[1,1],[1,0]]
    tet.append(e2)
    e3 = [[0,1,0],[1,1,1]]
    tet.append(e3)
    e4 = [[0,1],[1,1],[0,1]]
    tet.append(e4)

makeTet()

def ptn(si, sj, tt, tn, tm):
    # print()
    # print(f"si: {si}, sj: {sj}")
    sm = 0
    for i in range(si, si+tn):
        for j in range(sj, sj+tm):
            # print(f"i: {i}, j: {j}")
            if tt[i-si][j-sj] == 1:
                # print(f"graph[i][j]: {graph[i][j]}")
                sm += graph[i][j]
    # print(f"sm :{sm}")
    return sm

def match(tt):
    tn = len(tt)
    tm = len(tt[0])
    # print(f"tn: {tn}, tm: {tm}")

    mx = 0
    for i in range(N-tn+1):
        for j in range(M-tm+1):
            tmp = ptn(i, j, tt, tn, tm)
            mx = max(mx, tmp)
    return mx

# print(match([[1],[1],[1],[1]]))

res = 0
for t in tet:
    res = max(res, match(t))

print(res)



