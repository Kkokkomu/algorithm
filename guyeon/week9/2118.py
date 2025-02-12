import sys
from collections import deque
#3:30

input = sys.stdin.readline

left = deque()
right = deque()

leftCnt = rightCnt = 0

N = int(input())
for _ in range(N):
    left.append(int(input()))

mm = sum(left) # 전체 누적값
cannon = mm/2 # 기준값 - 이거 넘으면 절반 넘는거
# 일단 절반값 되기 직전까지 찾아놓음
while(mm > cannon):
    e = left.pop()
    mm-=e
    right.appendleft(e)
res = mm
print(f"after left: {left}, right: {right}, mm: {mm}, res: {res}")

# 이제 left연산 right 연산 끝까지 해보고 최소값 저장
while(leftCnt <= N-1 or rightCnt <= N-1):
    if right[-1] + mm <= cannon:
        print(f"after left: {left}, right: {right}, mm: {mm}, res: {res}")

        e = right.pop()
        mm += e
        left.appendleft(e)
        rightCnt+=1
        if mm > res:
            res = mm
    else:
        print(f"after left: {left}, right: {right}, mm: {mm}, res: {res}")

        if not left: # 4 1 1
            break
        e = left.pop()
        mm-=e
        right.appendleft(e)
        leftCnt+=1
    print()
print(res)
