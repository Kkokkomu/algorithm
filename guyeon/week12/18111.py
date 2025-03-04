#1230
import sys

input = sys.stdin.readline
INF = sys.maxsize

N,M,B = map(int, input().split())

graph=[]
cannon = 999
for _ in range(N):
    lll = list(map(int,input().split()))
    graph.append(lll)
    cannon = min(cannon, min(lll))

time = INF

def ck(cannon, B):
    add = 0
    rm = 0
    for i in range(N):
        for j in range(M):
            n = cannon - graph[i][j]
            if n > 0:
                add += n
            elif n < 0:
                rm += n
    B += (-rm)
    if add > B:
        return -1
    else:
        return add + (rm*(-2))


while True:
    tmp = ck(cannon, B)
    if tmp == -1 or tmp > time:
        print(str(time) + " " +str(cannon-1))
        exit()
    time = tmp
    cannon += 1
