# 1143 ~ 1231 257 318
# 1 10
import sys
import copy

input = sys.stdin.readline

def spin(si,sj,li): # 리스트안에 있는 좌표들을 특정 좌표를 기준으로 시계방향 회전
    res = []
    for ni, nj in li:
        ni -= si
        nj -= sj
        ni,nj = nj,ni
        ni *= -1
        ni += si
        nj += sj
        res.append([ni,nj])
    return res

def makeDcurve(): # 드래곤 커브 11계까지 생성
    dcurve = [[] for _ in range(11)]
    dcurve[0] = [[0,0],[1,0]]
    for i in range(1,11):
        dcurve[i] = dcurve[i-1] + list(reversed(spin(dcurve[i-1][-1][0], dcurve[i-1][-1][1], dcurve[i-1][:-1])))
    
    return dcurve

dcurve = makeDcurve()

N = int(input())

graph = [[0] * 101 for _ in range(101)]

def draw(dc, si, sj, dir): # 드래곤 커브가 주어지면 지도에 그리기
    for _ in range((-1*dir)%4): # 방향 맞춰서 회전시키기
        dc = spin(dc[0][0], dc[0][1], dc)
    for d in dc: # 시작 위치 따라서 커브 위치 반영
        d[0] += si
        d[1] += sj
        graph[d[0]][d[1]] = 1

for _ in range(N): 
    si, sj, dir, g = map(int, input().split())

    dc = copy.deepcopy(dcurve[g])
    draw(dc, si, sj, dir)

res = 0
for i in range(100): # 정사각형 갯수 구하기
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i+1][j+1] == 1 and graph[i][j+1] == 1:
            res+=1

print(res)

