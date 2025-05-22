#441
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
apple = set()
for _ in range(K):
    a, b = map(int,input().split())
    apple.add((a-1,b-1))

points = dict()
L = int(input())
for _ in range(L):
    X,C = input().split()
    X = int(X)
    points[X] = C

snack = deque([(0,0)])

di = [0,1,0,-1]
dj = [1,0,-1,0]
dir = 0
def front(dir):
    global N
    # print(f"dir: {dir}")

    ni, nj = snack[0]
    ni += di[dir]
    nj += dj[dir]
    if 0<= ni < N and 0<= nj < N\
        and ((ni,nj) not in snack):
        
        snack.appendleft((ni,nj))
        if (ni,nj) in apple:
            apple.remove((ni,nj))
            return 1
        else:
            return 0
    else:
        return -1

def back():
    snack.pop()

def go(dir):
    f = front(dir)
    if f == -1:
        return -1
    elif f == 0:
        back()

# print(points)
# print(apple)
cnt = 0
while True:
    cnt += 1
    # print(cnt)
    # print(snack)
    # print(f"dir: {dir}")
    
    if go(dir) == -1:
        print(cnt)
        break
    if cnt in points:
        d = points[cnt]
        if d == 'L':
            dir = (dir-1)%4
        else:
            dir = (dir+1)%4
    # print(snack)
    # print()