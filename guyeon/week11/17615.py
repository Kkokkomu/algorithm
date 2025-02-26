import sys
from collections import Counter

# 처음 시작되는 볼의 개수를 구하면 됨

# 1130
N = int(input())
balls = input().strip()

counter = Counter(balls)
cR = counter['R']
cB = counter['B']

# R로 시작
startB = balls[0]
startCnt = N
for i in range(1, N): # R은 처음부터 한 개만 연속됨
    if balls[i] != startB:
        startCnt = i
        break

if startCnt == N:
    print(0)
    exit()

# 좌측으로 R을 옮기게 된다면 5 - 1 개, B을 옮기게 된다면 4개
res1 = min(cR-startCnt, cB) if startB == 'R' else min(cB-startCnt, cR)

# R로 끝남
startB = balls[-1]
startCnt = N
for i in range(N-2,-1, -1): # R은 마지막부터 세 개만 연속됨
    if balls[i] != startB: 
        startCnt = N-i-1
        break
# 우측으로 R을 옮기게 된다면 5 - 3 개, B을 옮기게 된다면 4개
res2 = min(cR-startCnt, cB) if startB == 'R' else min(cB-startCnt, cR)

# 즉 답은 5-3 = 2개
print(min(res1, res2))

### rstrip lstrip을 이용하면 쉽게 풀리는 문제였다

# import sys

# N = int(sys.stdin.readline().strip())
# balls = str(sys.stdin.readline().strip())
# cnt = []

# # 우측으로 레드 모으기
# rexplore = balls.rstrip('R')
# cnt.append(rexplore.count('R'))

# # 우측으로 블루 모으기
# rexplore = balls.rstrip('B')
# cnt.append(rexplore.count('B'))

# # 좌측으로 레드 모으기
# lexplore = balls.lstrip('R')
# cnt.append(lexplore.count('R'))

# # 좌측으로 블루 모으기
# lexplore = balls.lstrip('B')
# cnt.append(lexplore.count('B'))

# print(min(cnt))