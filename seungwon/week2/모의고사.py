def solution(answers):
    # 각 수포자별 찍는 패턴 배열
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 각 배열 순회를 위한 인덱스 선언
    idx1 = idx2 = idx3 = 0
    # 각 수포자별 점수 배열
    score = [0, 0, 0]

    for a in answers:
        # 정답을 맞힌 경우 점수 1증가
        if a == man1[idx1]:
            score[0] += 1
        if a == man2[idx2]:
            score[1] += 1
        if a == man3[idx3]:
            score[2] += 1
        # 패턴 배열을 반복적으로 순회할 수 있도록 idx 증가시킴
        idx1 = (idx1 + 1) % 5
        idx2 = (idx2 + 1) % 8
        idx3 = (idx3 + 1) % 10

    # 최고점자 배열을 생성 후 리턴
    max_score = max(score)
    return [i + 1 for i in range(len(score)) if score[i] == max_score]
