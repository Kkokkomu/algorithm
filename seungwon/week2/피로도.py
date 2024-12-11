from itertools import permutations


def solution(k, dungeons):
    answer = -1

    # 던전 탐험 순서의 모든 경우의 수를 구함
    for li in permutations(range(len(dungeons))):
        temp_k = k
        count = 0
        # 특정 순서대로 던전을 돌때 최대 몇번 탐험할 수 있는지 계산
        for i in li:
            a, b = dungeons[i]
            if temp_k < a:
                break
            temp_k -= b
            count += 1
        # 완전탐색을 하며 최대 값을 구함
        answer = max(answer, count)

    return answer
