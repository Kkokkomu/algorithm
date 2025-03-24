# 다리 - 덱
# 다리 현재 하중
# 0610
# 다리 현재 트럭 수
import sys
from collections import deque

input = sys.stdin.readline

n,L,w = map(int,input().split())
trucks = list(reversed(list(map(int,input().split()))))

brdg = deque([0] * L)
brdg[-1] = trucks.pop()
bwei = brdg[-1]

res = 1
while trucks or bwei != 0:
    res += 1

    bwei -= brdg.popleft()

    if trucks and trucks[-1] + bwei <= w:
        brdg.append(trucks.pop())
        bwei += brdg[-1]
    else:
        brdg.append(0)

print(res)