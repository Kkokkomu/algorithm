#0951
import sys

input = sys.stdin.readline

N=int(input())

res = 0

pols = []
pc=0
for i in range(N):
    pols.append(list(map(int,input().split())))
    pc = max(pc, pols[i][1]) # 젤 높은 기둥 높이 저장

pols.sort()

highs =[]
for p in pols: # 젤 높은 기둥들 저장하고
    if p[1]==pc:
        highs.append(p)
startH = highs[0][0] # 처음 인덱스와 마지막 인덱스 저장
endH = highs[-1][0]+1

res += (endH-startH)*pc # 젤 높은 기둥들끼리 지붕 편성

upPols = [pols[0]] # 처음기둥 -> 젤 높은 기둥 올라가면서 쓸 기둥만 저장
cnn = pols[0][1]
for i in range(1, N):
    if pols[i][1] >= cnn:
        if pols[i][1] == pc:
            break
        cnn = pols[i][1]
        upPols.append(pols[i])

downPols = [pols[-1]] # 마지막기둥 -> 젤 높은 기둥 올라가면서 쓸 기둥만 저장
cnn = pols[-1][1]
for i in range(N-2, 0, -1):
    if pols[i][1] >= cnn:
        if pols[i][1] == pc:
            break
        cnn = pols[i][1]
        downPols.append(pols[i])

for i in range(1, len(upPols)): # 상승하는 지붕 면적 계산
    res += (upPols[i][0] - upPols[i-1][0])*upPols[i-1][1]
res += (highs[0][0] - upPols[-1][0])*upPols[-1][1]

for i in range(len(downPols)-1): # 하강하는 지붕 면적 계산
    res += (downPols[i][0] - downPols[i+1][0])*downPols[i][1]
res += (downPols[-1][0] - highs[-1][0])*downPols[-1][1]

print(res)