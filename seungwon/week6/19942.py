import itertools

N = int(input())
A, B, C, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
max_val = 9999999
answer = []

# 모든 경우의 수를 다 구해보기
for i in range(1, N + 1):
    for c in itertools.combinations(range(N), i):
        temp = []
        tempA = 0
        tempB = 0
        tempC = 0
        tempD = 0
        tempCost = 0

        for e in c:
            temp.append(e + 1)
            a, b, c, d, cost = li[e]
            tempA += a
            tempB += b
            tempC += c
            tempD += d
            tempCost += cost

        # 조건에 맞는지 확인
        if (
            tempA >= A
            and tempB >= B
            and tempC >= C
            and tempD >= D
            and tempCost <= max_val
        ):
            # 최소 비용을 가진 경우를 찾기
            if not answer:
                answer = temp[:]
            elif tempCost < max_val:
                answer = temp[:]
            # 비용이 같은 경우, 사전순으로 더 빠른 경우를 찾기
            elif "".join(map(str, sorted(temp))) < "".join(map(str, sorted(answer))):
                answer = temp[:]
            max_val = tempCost

if max_val == 9999999:
    print(-1)
else:
    print(max_val)
    print(*answer)
