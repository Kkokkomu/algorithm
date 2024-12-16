def solution(name):
    answer = 0
    index_li = []
    name_len = len(name)

    # 문자를 순회하며 커서이동이 필요한 문자의 index를 저장하고
    # 문자 변경을 하는데 필요한 횟수를 계산
    for i, a in enumerate(name):
        # 커서이동이 필요한 문자의 index 저장
        if a != "A" and i != 0:
            index_li.append(i)

        # 문자 변경을 하는데 필요한 횟수를 계산
        # 정방향으로 조작하는 경우
        gap1 = ord(a) - ord("A")
        # 역방향으로 조작하는 경우
        gap2 = (26 - gap1) % 26
        answer += min(gap1, gap2)

    # 최솟값으로 커서이동을 할 때의 횟수를 계산
    # 시작점 기준으로 오른쪽으로 이동할때 더 빨리 갈 수 있는 경우는 r_li에 저장
    # 시작점 기준으로 왼쪽으로 이동할때 더 빨리 갈 수 있는 경우는 l_li에 저장
    r_li = []
    l_li = []
    for idx in index_li:
        r_gap = idx
        l_gap = (name_len - r_gap) % name_len
        gap = min(r_gap, l_gap)
        if gap == r_gap:
            r_li.append(r_gap)
        else:
            l_li.append(l_gap)

    # 이동횟수에 따라 정렬
    r_li.sort()
    l_li.sort()

    # r_li 요소들을 먼저 방문할때 최소값
    r_move = 0
    if r_li:
        # r_li 요소들을 전부 방문
        r_move += r_li[-1]
    if l_li:
        # r_li 요소들을 전부 방문하고 난 후, l_li 요소들을 방문
        # 오른쪽으로 이동하여 방문할때와 왼쪽으로 이동하여 방문할때 중 최솟값을 적용
        r_move += min((l_li[-1] + r_move), (name_len - l_li[0] - r_move))

    # l_li 요소들을 먼저 방문할때 최소값
    l_move = 0
    if l_li:
        # l_li 요소들을 전부 방문
        l_move += l_li[-1]
    if r_li:
        # l_li 요소들을 전부 방문하고 난 후, r_li 요소들을 방문
        # 오른쪽으로 이동하여 방문할때와 왼쪽으로 이동하여 방문할때 중 최솟값을 적용
        l_move += min((r_li[-1] + l_move), (name_len - r_li[0] - l_move))

    answer += min(r_move, l_move)

    return answer
