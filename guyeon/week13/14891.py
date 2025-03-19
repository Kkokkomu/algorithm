#0122 ~ 0215
import sys

input = sys.stdin.readline

cirs = []
for _ in range(4):
    cirs.append(list(map(int,list(input().rstrip()))))

def spin(idx, dir): # 특정 방향으로 톱니 회전
    dir*=-1
    tmp = cirs[idx][0]
    for i in range(7):
        cirs[idx][i*dir] = cirs[idx][((i+1)*dir)]
    cirs[idx][dir*-1] = tmp

K= int(input())    
cmds=[]
for _ in range(K):
    cmds.append(list(map(int,input().split())))

tmpCmds=[]
def addCmdsR(idx, dir): # 오른쪽에 돌아갈 톱니 있으면 명령 스택에 추가
    for i in range(idx,3):
        if cirs[i][2] == cirs[i+1][6]:
            break
        dir *= -1
        tmpCmds.append((i+1,dir))
def addCmdsL(idx, dir): # 왼쪽에 돌아갈 톱니 있으면 명령 스택에 추가
    for i in range(idx,0,-1):
        if cirs[i][6] == cirs[i-1][2]:
            break
        dir *= -1
        tmpCmds.append((i-1,dir))
def addCmds(idx, dir): # 돌아갈 톱니 기준으로 왼쪽 오른쪽 톱니 탐색
    tmpCmds.append((idx,dir))
    addCmdsR(idx,dir)
    addCmdsL(idx,dir)
def execCmds(): # 명령 스택에 있는 명령들따라서 톱니 회전
    for cmd in tmpCmds:
        spin(cmd[0],cmd[1])

for cmd in cmds: # 메인 명령 하나씩 수행
    tmpCmds=[]
    addCmds(cmd[0]-1,cmd[1])
    execCmds()

res=0 # 점수 계산
if cirs[0][0]==1:
    res+=1
if cirs[1][0]==1:
    res+=2
if cirs[2][0]==1:
    res+=4
if cirs[3][0]==1:
    res+=8
print(res)