# 1950
# itertools로 경계값 뽑기
# 케이스 마다 슬라이싱해서 최대 최소 구하기

import sys
from itertools import combinations

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))
if M==1:
    print(max(li)-min(li))
    exit()

bry = []
def dfs(depth, idx):
    global res
    if depth == M-1:
        slc = li[0:bry[0]]

        sm = max(slc) - min(slc)
        for i in range(M-2):
            slc = li[bry[i]:bry[i+1]]
            tmp = max(slc) - min(slc)
            if tmp > sm:
                sm = tmp
        slc = li[bry[M-2]:N]

        tmp = max(slc) - min(slc)
        if tmp > sm:
            sm = tmp
        
        if sm < res:
            res = sm
    else:
        for i in range(idx+1,N):
            bry.append(i)
            dfs(depth+1, i)
            bry.pop()


res = 99999
dfs(0,0)

print(res)
