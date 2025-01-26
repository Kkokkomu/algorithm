import sys

N = int(sys.stdin.readline())

move = [(1,1), (-1,-1), (1,-1), (-1,1)]

board = [[False] * N for _ in range(N)]

visited = [False]*N

res = 0

def isSafe(si, sj):
    for mi, mj in move:
        n=1
        while 0<= si + mi*n <si and 0<= sj + mj*n <N:
            if board[si + mi*n][sj + mj*n]:
                return False
            n+=1
    
    return True

def dfs(level):
    global res
    if level == N:
        res += 1
        # for i in range(N):
        #     print(board[i])
        # print()
        return
    for i in range(N):
        if visited[i] or isSafe(level, i) == False:
            continue
        board[level][i] = True
        visited[i] = True
        dfs(level+1)
        visited[i] = False
        board[level][i] = False

dfs(0)

print(res)