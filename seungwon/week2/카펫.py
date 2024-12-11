def solution(brown, yellow):
    answer = [0, 0]

    # yellow 약수 구해서
    # yellow 배치 가능한 모든 경우의 수 구하기
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i != 0:
            continue
        # 주어진 yellow의 가능한 width와 height 경우 구하기
        # 가로가 세로보다 길거나 같음
        y_w = yellow // i
        y_h = i

        # 가정한 yellow의 width와 height를 통해 brown의 개수를 구함
        b_w = y_w + 2
        b_h = y_h + 2
        b_count = b_w * 2 + b_h * 2 - 4

        # 계산한 b_count가 주어진 brown 개수와 같으면
        # 이때 가정한 [b_w, b_h]이 정답
        if b_count == brown:
            answer[0], answer[1] = b_w, b_h
            break

    return answer
