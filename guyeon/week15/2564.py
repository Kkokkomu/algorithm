#1108
# 좌표화
# 동근이 반대편, 사이드를 저장해두기
# 사이드면 정해져잇음
# 같은쪽이면 절대값
# 반대편이면 x, n-x 비교

import sys

input = sys.stdin.readline

C,R = map(int,input().split())
N = int(input())
graph = []
for _ in range(N):
    a,b= map(int,input().split())
    if a==1:
        graph.append(((R,b),a,b))
    elif a==2:
        graph.append(((0,b),a,b))
    elif a==3:
        graph.append(((R-b,0),a,b))
    elif a==4:
        graph.append(((R-b,C),a,b))

xi = xj = 0
dir, n = map(int,input().split())
if dir==1:
    xi=R
    xj=n
    dir_f = 2
    slid = C
    side = R
elif dir==2:
    xi=0
    xj=n
    dir_f = 1
    slid = C
    side = R
elif dir==3:
    xi=R-n
    xj=0
    dir_f = 4
    slid = R
    side = C
elif dir==4:
    xi=R-n
    xj=C
    dir_f = 3
    slid = R
    side = C

res = 0
for g in graph:
    # print(res)
    d = g[1]
    dn = g[2]
    di = g[0][0]
    dj = g[0][1]

    if d==dir_f:
        res += (side + min((dn+n),(2*slid-dn-n)))
    else:
        res += (abs(xi-di) + abs(xj-dj))
print(res)