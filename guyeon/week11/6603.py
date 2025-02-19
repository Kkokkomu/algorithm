import sys

input = sys.stdin.readline

def dfs(depth,idx):
    if depth == 6:
        print(*out)
        return
    for i in range(idx, N):
        out.append(li[i])
        dfs(depth+1, i+1)
        out.pop()


while True:
    iinput = list(map(int,input().split()))
    N = iinput[0]
    if N==0:
        exit()
    li = iinput[1:]

    out = []
    dfs(0,0)
    print()

