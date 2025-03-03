# #0748~0908
# 오타 하나때문에 거의 40분은 날렸다..
# 문제에 대한 확신이 있으면 오타는 없는지 확인해보자
import sys

N,M = map(int,input().split())
si, sj, dir = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

di = [0,1,0,-1]
dj = [1,0,-1,0]

def isClean(si, sj): # 청소되지 않은 빈칸이 있으면 False, 없으면 True
    for i in range(4):
        ni = si + di[i]
        nj = sj + dj[i]
        if graph[ni][nj] == 0:
            return False
    return True

def moveBack(dir): # 뒤로 한 칸 후진 만약에 못하면 -1
    global si
    global sj

    ni = si
    nj = sj
    if dir == 0:
        ni+=1
    elif dir == 1:
        nj-=1
    elif dir == 2:
        ni-=1
    elif dir == 3:
        nj+=1
    if graph[ni][nj] != 1:
        si = ni
        sj = nj
        return True
    else:
        return False

def turnLeft(): # 반시계 방향으로 회전
    global dir
    dir = (dir-1)%4

def goStr(dir):
    global si
    global sj
    ni = si
    nj = sj

    if dir == 0:
        ni -= 1
    elif dir == 1:
        nj += 1
    elif dir == 2:
        ni += 1
    elif dir == 3:
        nj -= 1
    
    if graph[ni][nj] == 0:
        si = ni
        sj = nj
        return True
    else:
        return False

cnt = 0
while True:
    
    if graph[si][sj] == 0:
        graph[si][sj] = 9 # 현재칸이 아직 청소되지 않았으면, 현재 칸 청소
        cnt+=1
    if isClean(si, sj): # 청소되지 않은 빈칸이 주변에 없는 경우 
        if moveBack(dir) == False: # 후진도 못하면 작동중지
            break
    else: # 청소되지 않은 빈칸이 주변에 있는 경우
        for _  in range(4):
            turnLeft() # 일단 반시계 회전
            if goStr(dir): # 앞으로 갈 수 있다면 가기
                break

print(cnt)