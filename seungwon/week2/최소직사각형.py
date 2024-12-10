def solution(sizes):
    # 최대 넓이 및 높이
    max_w = 0
    max_h = 0

    for w, h in sizes:
        # 세로 높이가 더 크다면 카드를 돌려서
        # 무조건 가로 높이가 더 크게 만든다
        if w < h:
            w, h = h, w
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h
