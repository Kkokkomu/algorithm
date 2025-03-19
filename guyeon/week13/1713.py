# 1223
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

recs = list(map(int,input().split()))

pics = [[recs[0],1]]

def minPics():
    mn = 9999
    for p in pics:
        if p[1] < mn:
            mn = p[1]
    return mn

def ifin(rec):
    for pic in pics:
        if pic[0] == rec:
            pic[1] += 1
            return True
    return False

for i in range(1,M):
    if ifin(recs[i]):
        continue

    if len(pics) < N:
        pics.append([recs[i],1])
    else:
        minRc = minPics()
        for j in range(N):
            if minRc == pics[j][1]:
                del pics[j]
                pics.append([recs[i],1])
                break

pics.sort()
for p in pics:
    print(p[0],end=" ")