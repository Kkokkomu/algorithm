import sys

# 배열 하나를 set으로
# 나머지 배열을 순회하면 in 연산자로 찾음
# 교차점을 찾을때마다 이전 교차점부터 지금의 교차점까지 더 적은걸 더함
# 이전 교차점의 초기값은 0

input = sys.stdin.readline

while True:
    r1 = list(map(int,input().split()))
    if r1[0] == 0:
        break
    r2 = list(map(int,input().split()))

    r1 = r1[1:]
    r2 = r2[1:]

    setr1 = set(r1)
    setr2 = set(r2)
    inter1 = []
    inter2 = []
    interCnt = 0
    for i in range(len(r1)): # r1부터 상대 교차점과 곂치는 부분의 인덱스를 교차점 배열에 저장
        if r1[i] in setr2:
            inter1.append(i)
            interCnt+=1
    for i in range(len(r2)): # r2도 상대 교차점과 곂치는 부분의 인덱스를 교차점 배열에 저장
        if r2[i] in setr1:
            inter2.append(i)

    res = 0
    if interCnt != 0:
        res += max(sum(r1[:inter1[0]]), sum(r2[:inter2[0]]))
        for i in range(1, interCnt):
            res += max(sum(r1[inter1[i-1]:inter1[i]]), sum(r2[inter2[i-1]:inter2[i]]))
        res += max(sum(r1[inter1[interCnt-1]:]), sum(r2[inter2[interCnt-1]:]))
    else:
        res = max(sum(r1), sum(r2))
    print(res)