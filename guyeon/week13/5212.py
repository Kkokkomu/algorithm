# 잠기는지 판별하는 함수 -> 새 지도에 . 으로 표시
# 새 지도를 자르는 함수
# 0508
import sys

input = sys.stdin.readline

di = [0,1,0,-1]
dj = [1,0,-1,0]

N,M = map(int,input().split())

graph=[['.']*(M+2)]
for _ in range(N):
    li = list("." + input().rstrip() + '.')
    graph.append(li)
graph.append(['.']*(M+2))

def isend(si,sj):
    cnt=0
    for i in range(4):
        ni = si+di[i]
        nj = sj+dj[i]

        if graph[ni][nj] == '.':
            cnt+=1
    if cnt >= 3:
        return True
    else:
        return False

newMap = [g[:] for g in graph]

for i in range(1,N+1):
    for j in range(1,M+1):
        if isend(i,j):
            newMap[i][j] = '.'

# 행 삭제
start = N+2
end = 0
for i in range(N+2):
    if 'X' in newMap[i]:
        start = i
        break
for i in range(N+1, -1, -1):
    if 'X' in newMap[i]:
        end = i+1
        break
newMap = newMap[start:end]

# 열 삭제
start = M+2
end = 0
for g in newMap:
    for i in range(M+2):
        if g[i] == 'X':
            start = min(start, i)
            break
    for i in range(M+1, -1, -1):
        if g[i] == 'X':
            end = max(end, i+1)
            break
res = []
for g in newMap:
    res.append(g[start:end])

for r in res:
    print("".join(r))