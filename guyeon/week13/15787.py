#1428
import sys
from collections import deque

input = sys.stdin.readline

N,M=map(int, input().split())

trains = [deque([0]*20) for _ in range(N+1)]

for _ in range(M):
    cmd = input()
    if cmd[0]=='1' or cmd[0]=='2':
        a,b,c = map(int,cmd.split())

        if a == 1:
            if trains[b][c-1] == 0:
                trains[b][c-1] = 1
        if a == 2:
            if trains[b][c-1] == 1:
                trains[b][c-1] = 0
    else:
        a,b = map(int,cmd.split())

        if a == 3:
            trains[b].pop()
            trains[b].appendleft(0)
        if a == 4:
            trains[b].popleft()
            trains[b].append(0)
res = 0
li = []
for train in trains[1:]:
    if train not in li:
        li.append(train)
        res+= 1
print(res)