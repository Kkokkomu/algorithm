import sys

sys.setrecursionlimit(10**6)

N=int(input())

input = sys.stdin.readline

tr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    tr[a].append(b)
    tr[b].append(a)

ans= [0]*(N+1)

def dfs(x):
    for n in tr[x]:
        if ans[n]==0:
            ans[n]=x
            dfs(n)
dfs(1)
for i in range(2,N+1):
    print(ans[i])