#1639

import sys

input = sys.stdin.readline

r,c,k = map(int,input().split())

R = [[0] * 100 for _ in range(100)]
C = [[0] * 100 for _ in range(100)]

maxR = 3
maxC = 3

for i in range(3):
    a,b,d = map(int,input().split())
    R[i][0] = C[0][i] = a
    R[i][1] = C[1][i] = b
    R[i][2] = C[2][i] = d

def caltp(arr):

    res = []

    cnt = 1
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            res.append((cnt,arr[i-1]))
            cnt=1
        else:
            cnt+=1
    
    res.append((cnt,arr[-1]))

    return res

def calCol(mt, idx):
    if mt == 0:
        arr = R[idx]
    elif mt == 1:
        arr = C[idx]
    arr.sort(reverse=True)
    if arr[-1] == 0:
        arr = arr[:arr.index(0)]

    tp = caltp(arr)
    tp.sort()

    res = []
    for t in tp:
        res.append(t[1])
        res.append(t[0])
    
    if len(res) >= 100:
        return res[:100]
    return res

def cal(mt):
    global maxR,maxC

    if mt == 0:
        maxC = 0
        for i in range(maxR):
            arr = calCol(0,i)
            arr_len = len(arr)

            for j in range(arr_len):
                R[i][j] = arr[j]
                C[j][i] = arr[j]
            for j in range(arr_len,100):
                R[i][j] = 0
                C[j][i] = 0

            maxC = max(maxC, arr_len)

    elif mt == 1:
        maxR=0
        for i in range(maxC):
            arr = calCol(1,i)
            arr_len = len(arr)

            for j in range(arr_len):
                C[i][j] = arr[j]
                R[j][i] = arr[j]
            for j in range(arr_len,100):
                C[i][j] = 0
                R[j][i] = 0

            maxR = max(maxR, arr_len)

cnt=0
while R[r-1][c-1] != k:
    if maxR >= maxC:
        cal(0)
    else:
        cal(1)
    cnt+=1
    if cnt == 101:
        print(-1)
        exit()

print(cnt)