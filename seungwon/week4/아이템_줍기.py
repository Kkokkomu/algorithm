from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 유효한 좌표들
    valid_coordinate = set()
    # rectangle에서 나오는 좌표들
    temp = set()

    # rectangle의 좌표들을 temp에 추가
    # 각 좌표들을 0.5 단위로 나누어 추가
    # 예를 들어 (1, 1, 2, 2) -> (1, 1), (1, 1.5), (1, 2), (1.5, 1), (1.5, 1.5), (1.5, 2), (2, 1), (2, 1.5), (2, 2)
    # ㄷ자 형태의 경로가 만들어졌을때 의도치 않은 경로로 이동하는 것을 방지
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2 + 1):
            temp.add((i, y1))
            temp.add((i, y2))
            if i + 0.5 <= x2:
                temp.add((i + 0.5, y1))
                temp.add((i + 0.5, y2))
        for j in range(y1, y2 + 1):
            temp.add((x1, j))
            temp.add((x2, j))
            if j + 0.5 <= y2:
                temp.add((x1, j + 0.5))
                temp.add((x2, j + 0.5))

    # temp 좌표들이 다른 rectangle 안에 있는지 검사
    # 다른 rectangle 안에 있지 않은 좌표만 유효한 좌표
    for x, y in temp:
        for r_x1, r_y1, r_x2, r_y2 in rectangle:
            if r_x1 < x < r_x2 and r_y1 < y < r_y2:
                break
        else:
            valid_coordinate.add((x, y))

    # BFS
    # (count, x, y)의 형태로 큐에 저장
    dq = deque([(0, characterX, characterY)])
    # 동서남북으로 이동
    x_shift = [0.5, -0.5, 0, 0]
    y_shift = [0, 0, -0.5, 0.5]

    while dq:
        # count: 이동 횟수, x, y: 현재 좌표
        count, x, y = dq.popleft()
        # 이미 방문한 좌표는 제외
        if (x, y) not in valid_coordinate:
            continue
        # 방문한 좌표는 제외
        valid_coordinate.remove((x, y))

        # 아이템을 찾으면 count를 2로 나눈 값을 반환
        # 좌표를 0.5 단위로 나누었기 때문에 count를 2로 나누어야 함
        if x == itemX and y == itemY:
            answer = count // 2
            break

        # 동서남북으로 이동
        for i in range(4):
            next_x, next_y = x + x_shift[i], y + y_shift[i]
            if (next_x, next_y) in valid_coordinate:
                dq.append((count + 1, next_x, next_y))

    return answer
