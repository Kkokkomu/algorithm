#1042 ~ 1114
import sys

input = sys.stdin.readline

N,M,si,sj,K = map(int,input().split())

graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

cmds = list(map(int,input().split()))

dice = [0]*6 # 주사위는 1차원 배열로 표현

# 이동방향에 따라 주사위 굴러가는거 반영
def cgDice(dir):
    if dir == 1:
        tmp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = tmp
    elif dir == 2:
        tmp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp
    elif dir == 3:
        tmp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = tmp
    elif dir == 4:
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp

# 이동방향에 따라 주사위 좌표 반영
def cgLoc(dir):
    global si
    global sj
    ni = si
    nj = sj

    if dir == 1:
        nj += 1
    elif dir == 2:
        nj -= 1
    elif dir == 3:
        ni -= 1
    elif dir == 4:
        ni += 1
    
    if 0 <= ni < N and 0<= nj < M: # 맵 안에서 움직인 건지 확인
        si = ni
        sj = nj
        return True
    return False

# 주어진 방향으로 이동
def go(dir):
    if cgLoc(dir):
        cgDice(dir)
        if graph[si][sj] == 0: # 움직였는데 바닥이 0이면
            graph[si][sj] = dice[0] # 주사위 바닥 복사
        else:
            dice[0] = graph[si][sj] # 아니면 주사위 바닥에 복사
            graph[si][sj] = 0 # 타일은 0으로
        print(dice[5]) # 주사위 윗 부분 출력

for cmd in cmds:
    go(cmd)