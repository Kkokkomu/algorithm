#0248
import sys

input = sys.stdin.readline

N=int(input())
cmds = list(input().rstrip())

graph = [['@'] * 101 for _ in range(101)]
ci = 50
cj = 50
graph[ci][cj] = '.'

dir = 0

def rotatR(): # 오른쪽회전
    global dir

    dir = (dir+1)%4

def rotatL(): # 왼쪽회전
    global dir

    dir = (dir-1)%4

def go(): # 앞으로가기
    global dir
    global ci
    global cj

    if dir == 0:
        ci += 1
    elif dir == 1:
        cj -= 1
    elif dir == 2:
        ci -= 1
    elif dir == 3:
        cj += 1
    graph[ci][cj] = '.'

for cmd in cmds: # 명령들 수행
    if cmd == 'R':
        rotatR()
    elif cmd == 'L':
        rotatL()
    elif cmd == 'F':
        go()

mni = mnj = 50
mxi = mxj = 50

for i in range(101): # 수행된 맵 크기 계산
    for j in range(101):
        if graph[i][j] == '.':
            mni = min(mni, i)
            mnj = min(mnj, j)
            mxi = max(mxi, i)
            mxj = max(mxj, j)

for i in range(mni, mxi+1): # 수행된 부분만 추출하고 나머진 벽으로 출력
    for j in range(mnj,mxj+1):
        if graph[i][j] == '@':
            graph[i][j] = '#'
    print("".join(graph[i][mnj:mxj+1]))
