from collections import deque

answer = 0
R, C = map(int, input().split())
forest = [[e for e in input()] for _ in range(R)]
# 물 방문 여부, 고슴도치 방문 여부
water_is_visited = [[False] * C for _ in range(R)]
s_is_visited = [[False] * C for _ in range(R)]
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]
dq = deque()
si = sj = 0

# 초기화
# 물과 고슴도치의 위치를 큐에 넣어준다
# 물이 퍼지게 될 곳에는 고슴도치가 이동할 수 없으므로 물이 있는 곳을 먼저 큐에 넣어준다
for i, row in enumerate(forest):
    for j, e in enumerate(row):
        if e == "*":
            dq.append((i, j, "*", 0))
        elif e == "S":
            si, sj = i, j
dq.append((si, sj, "S", 0))

while dq:
    # i, j: 현재 위치
    # e: 현재 위치의 값
    # cost: 현재 위치까지의 비용 (현재 원소가 물인 경우는 0, 사용안함)
    i, j, e, cost = dq.popleft()

    # 큐에서 꺼낸 원소가 물인 경우
    # 물이 퍼지는 방향으로 큐에 넣어준다
    if e == "*":
        if water_is_visited[i][j]:
            continue
        water_is_visited[i][j] = True
        # 물이 퍼지는 방향으로 큐에 넣어준다
        for d in range(4):
            next_i = i + di[d]
            next_j = j + dj[d]
            if (
                0 <= next_i < R
                and 0 <= next_j < C
                and not water_is_visited[next_i][next_j]
                # 현재 고슴도치가 있는 곳에도 다음 시간에 물이 찰 수 있으므로 고슴도치가 있는 곳도 물이 찰 수 있게 해준다
                and (forest[next_i][next_j] == "." or forest[next_i][next_j] == "S")
            ):
                # 물이 퍼지는 방향으로 큐에 넣어주고, 해당 위치를 물로 바꿔준다
                forest[next_i][next_j] = "*"
                dq.append((next_i, next_j, "*", 0))
    # 큐에서 꺼낸 원소가 고슴도치인 경우
    # 고슴도치가 이동할 수 있는 방향으로 큐에 넣어준다
    elif e == "S":
        if s_is_visited[i][j]:
            continue
        s_is_visited[i][j] = True
        for d in range(4):
            next_i = i + di[d]
            next_j = j + dj[d]
            if 0 <= next_i < R and 0 <= next_j < C and not s_is_visited[next_i][next_j]:
                # 다음 위치가 비어있는 경우, 큐 원소로 'S'를 넣어준다
                # 다음 위치가 비버의 굴인 경우, 큐 원소로 'D'를 넣어준다
                # cost에 1을 더해준다
                if forest[next_i][next_j] == ".":
                    dq.append((next_i, next_j, "S", cost + 1))
                elif forest[next_i][next_j] == "D":
                    dq.append((next_i, next_j, "D", cost + 1))
    # 큐에서 꺼낸 원소가 D인 경우
    # 즉, 고슴도치가 비버의 굴에 도착한 경우
    else:
        answer = cost
        break

# 고슴도치가 비버의 굴에 도착하지 못한 경우
if answer == 0:
    answer = "KAKTUS"

print(answer)
