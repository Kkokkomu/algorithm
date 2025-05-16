#2124
import sys

input = sys.stdin.readline

N = int(input())
graph = [[]]
for _ in range(N):
    graph.append([0] + list(map(int, sys.stdin.readline().split())))

def cnt_all(si, sj, d1, d2):
    print(f"si: {si}, sj: {sj}, d1: {d1}, d2: {d2}")
    res = []

    cnt = 0 #1
    for i in range(1,si):
        cnt += sum(graph[i][1:sj+1])
    for i in range(si,si+d1):
        cnt += sum(graph[i][1:sj-(i-si)])
    res.append(cnt)

    cnt=0 #2
    for i in range(1,si):
        cnt += sum(graph[i][sj+1:N+1])
    for i in range(si,si+d2+1):
        cnt += sum(graph[i][sj+1+i-si:N+1])
    res.append(cnt)

    cnt=0 #3
    for i in range(si+d1, si+d1+d2+1):
        print(f"i: {i}")
        cnt += sum(graph[i][1:sj-d1+i-(si+d1)])
    for i in range(si+d1+d2+1,N+1):
        cnt += sum(graph[i][1:sj])
    res.append(cnt)

    cnt=0 #4
    for i in range(si+d2+1,si+d1+d2+1):
        cnt += sum(graph[i][sj+d2-(i-(sj+d2)):N+1])
    for i in range(si+d2+d1+1,N+1):
        cnt += sum(graph[i][sj:])
    res.append(cnt)

    cnt=0
    s=sj
    e=sj+1
    for i in range(si+1, si+d1+d2):
        cnt += sum(graph[i][s:e])

        if i < si + d1:
            s-=1
        else:
            s+=1
        
        if i < si + d2:
            e+=1
        else:
            e-=1
    res.append(cnt)

    print(f"max(res) - min(res): {max(res) - min(res)}")

    return max(res) - min(res)

res = sys.maxsize
for x in range(1, N+1):
        for y in range(1, N+1):
            for d1 in range(1, N+1):
                for d2 in range(1, N+1):
                    if 1 <= x < x+d1+d2 <= N  and 1 <= y-d1 < y < y+d2 <= N:
                        res = min(res, cnt_all(x, x, d1, d2))

print(res)