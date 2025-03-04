import sys

input = sys.stdin.readline

N,M=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(input().rstrip()))

cnn = min(N,M)

def ck(n):
    # print(f"n: {n}")
    for i in range(N-n+1):
        for j in range(M-n+1):
            if graph[i][j] == graph[i][j+n-1] == graph[i+n-1][j] == graph[i+n-1][j+n-1]:
                # print(f"i: {i}, j: {j}")
                # print(f"i: {i}, j+n-1: {j+n-1}")
                # print(f"i+n-1: {i+n-1}, j: {j}")
                # print(f"i+n-1: {i+n-1}, j+n-1: {j+n-1}")
                return True
    return False

res = 1
for i in range(2, cnn+1):
    if not ck(i):
        continue
    res = i
print(res**2)