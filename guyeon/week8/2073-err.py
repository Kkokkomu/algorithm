import sys
from collections import deque

input = sys.stdin.readline

D, P = map(int,input.split())

pips = [list(map(int, input.split())) for _ in range(P)]

if P==1:
    print(pips[0][1])
    exit()

# print(pips)

pips.sort(key=lambda x : (-x[1], -x[0]))

# print(pips)

dp = deque()

for i in range(1, P):

# 누적 값에서 D를 안넘는 값이 있으면 큐에 넣기
    l = len(dp)
    for _ in range(l):
        p=dp.popleft()
        if p + pips[i][0] < D:
            dp.append(p + pips[i][0])
        elif p + pips[i][0] == D:
            print(pips[i][1])
            exit()

    for j in range(i):
        if pips[i][0] + pips[j][0] < D:
            dp.append(pips[i][0] + pips[j][0])
        elif pips[i][0] + pips[j][0] == D:
            print(pips[i][1])
            exit()
