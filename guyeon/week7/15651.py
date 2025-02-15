import sys

N, M = map(int, sys.stdin.readline().split())

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()
    return
dfs()