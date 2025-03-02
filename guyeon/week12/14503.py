# #0748
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
    
def pr():
    print()
    for g in graph:
        print(g)

cnt = 0
while True:
    
    if graph[si][sj] == 0:
        graph[si][sj] = 9 # 현재칸이 아직 청소되지 않았으면, 현재 칸 청소
        cnt+=1
    # pr()
    if isClean(si, sj): # 청소되지 않은 빈칸이 주변에 없는 경우 
        # print("flse")
        if moveBack(dir) == False: # 후진도 못하면 작동중지
            break
    else: # 청소되지 않은 빈칸이 주변에 있는 경우
        for _  in range(4):
            turnLeft() # 일단 반시계 회전
            if goStr(dir): # 앞으로 갈 수 있다면 가기
                # print(dir)
                break

print(cnt)

# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# area = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# def pr():
#     print()
#     for a in area:
#         print(a)

# # 본 문제에서는 없어도 통과되지만, 범위 안에서 이동하는지 확인하기 위해 필요함
# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m


# def cleaner(x, y, d):
#     cnt = 0
#     while True:
        
#         # 1번 청소하고 청소 횟수 1 증가
#         if area[x][y] == 0:
#             area[x][y] = 9 # 청소함
#             cnt += 1
#         pr()
#         # 3번 반시계 방향으로 회전하며 청소하지 않은 칸 탐색
#         for _ in range(4):
#             d = (d - 1) % 4
#             nx, ny = x + dx[d], y + dy[d]
#             if in_range(nx, ny) and area[nx][ny] == 0:  # 청소 안한 칸으로 이동
#                 x, y = nx, ny
#                 break # 이동했으면 다시 1번으로

#         else:
#             print('a')
#             # 2번 4칸다 깨끗하다면 후진하거나 멈춤
#             x, y = x + dx[d] * (-1), y + dy[d] * (-1) # 후진
#             if in_range(x, y) and area[x][y] == 1 or not in_range(x,y):  # 벽이라면 작동 멈춤
#                 print(cnt)
#                 return

# cleaner(r, c, d)