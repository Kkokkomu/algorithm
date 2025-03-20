#1652 ~ 56 58 ~1720 1735~1748 1755~611
import sys

input = sys.stdin.readline

N,M,H = map(int,input().split())

ladds = [[i] * (H+1) for i in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    ladds[b][a] = b+1
    ladds[b+1][a] = b

def side(n):
    cur = n
    for i in range(1, H+1):
        cur = ladds[cur][i]
        
    return cur

def simul():
    # print()
    # print(ladds)
    for i in range(1,N+1):
        if i != side(i):
            return False
        # print(i)
    return True

def pt():
    for l in ladds:
        print(l)

res = 4
def dfs(depth):
    global res
    if depth == 4 or depth >= res:
        return 4
    for i in range(1, N):
        for j in range(1, H+1):
            if ladds[i][j] == i:
                if ladds[i+1][j]==i+1: # 오른쪽에 가로추가 시도
                    ladds[i][j] = i+1
                    ladds[i+1][j] = i
                    if simul():
                        res = min(res,depth)
                    dfs(depth+1)
                    ladds[i][j] = i
                    ladds[i+1][j] = i+1

if simul():
    print(0)
else:
    dfs(1)
    if res==4:
        print(-1)
    else:
        print(res)