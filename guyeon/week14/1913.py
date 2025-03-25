# 0221~0251
import sys

N = int(sys.stdin.readline())
tg = int(sys.stdin.readline())

snail = [[0] * N for _ in range(N)]

si = sj = N//2
snail[si][sj] = 1
n = 1

di = [0,1,0,-1]
dj = [1,0,-1,0]
def pt():
    for s in snail:
        print(*s, sep=' ')
    
for i in range(1,N//2+1):
    si -= 1
    mul = i*2

    n+=1
    snail[si][sj] = n
    for _ in range(mul-1):
        sj+=1
        n+=1
        snail[si][sj] = n
    for j in range(1, 4):
        for _ in range(mul):
            si += di[j]
            sj += dj[j]
            n+=1
            snail[si][sj] = n
pt()
for i in range(N):
    for j in range(N):
        if snail[i][j] == tg:
            print(i+1, end=' ')
            print(j+1)

