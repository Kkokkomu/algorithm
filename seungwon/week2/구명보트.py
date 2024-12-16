from collections import deque


def solution(people, limit):
    answer = 0
    # people 리스트를 정렬한 후, 덱 구조로 전환
    people.sort()
    dq = deque(people)

    # 모든 사람을 구출할때까지 반복
    while dq:
        # 남은 사람이 1명이라면 짝 지을 사람이 없으므로
        # 혼자 타고 탈출
        if len(dq) < 2:
            dq.pop()
            answer += 1
            break

        # 남은 사람이 2명 이상인 경우
        # 제일 마른 사람과 제일 뚱뚱한 사람이 같이 탔을때 제한을 초과한다면
        # 제일 뚱뚱한 사람은 혼자타고 나가야 함
        # 제한을 초과하지 않는다면 둘이 같이 타고 나감
        if dq[0] + dq[-1] > limit:
            dq.pop()
        else:
            dq.popleft()
            dq.pop()

        answer += 1

    return answer
