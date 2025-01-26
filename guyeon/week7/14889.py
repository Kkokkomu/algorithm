import sys
from itertools import combinations

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        board[i][j]+=board[j][i]
# for b in board:
#     print(b)
res = 9999999

ll = [i for i in range(N)]
s=[]

def cal():
    global res
    li = combinations(s,2)
    ss = 0
    for a,b in li:
        # print(ss)
        # print(f"a: {a}, b: {b} : {board[a][b]}")
        # print(f"[N-b-1]: {N-b-1}, [N-a-1]: {N-a-1} : {-board[N-b-1][N-a-1]}")
        ss+=board[a][b]
    # print(f"ss : {abs(ss)}, res: {res}")
    # print()

    li = combinations(list(set(ll)-set(s)),2)
    lss=0
    for a,b in li:
        lss+=board[a][b]
    if abs(ss-lss) < res:
        res = abs(ss-lss)

def dfs(e):
    if len(s) == N//2:
        # print(s)
        cal()
        return 
    for i in range(e+1, N):
        s.append(i)
        dfs(i)
        s.pop()

for i in range(N//2):
    s.append(i)
    dfs(i)
    s.pop()

print(res)

