import sys

n = int(sys.stdin.readline())

glasses = [[int(sys.stdin.readline()),0,0] for _ in range(n)]

if n==1:
    print(glasses[0][0])
    exit()
if n==2:
    print(glasses[0][0]+glasses[1][0])
    exit()

glasses[0][1] = glasses[0][0]
glasses[0][2] = glasses[0][0]

glasses[1][1] = glasses[0][0] + glasses[1][0]
glasses[1][2] = glasses[1][0]

res = 0
for i in range(2,n):
    glasses[i][1] = glasses[i-1][2] + glasses[i][0]
    glasses[i][2] = max(glasses[i-2][1], glasses[i-2][2]) + glasses[i][0]
    # res = max(res, glasses[i][1], glasses[i][2])
    if res < glasses[i][1]:
        res = glasses[i][1]
    if res < glasses[i][2]:
        res = glasses[i][2]
print(res)

# dp의 값을 참조하려면 dp의 값이 최적의 값을 가지고 있어야 한다 -> dp 배열의 마지막 값이 답이어야 한다
# 반례: 예를들어 추가 데이터로 9잔, 6 10 13 9 8 1 1 2 4 라고 했을 때
# 기존 코드로는 dp 값이 [6 16 23 28 33 32 34 36 38] 이 됩니다. 문제가 생겼죠. 32가 아니라 33이 저장되어 33 + 2 + 4로 39가 되어야하는데 38이 결과로 나와버렸습니다.
# 6번째 값이 최적이 아니라서 그럼