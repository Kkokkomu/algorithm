def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    # 여벌 체육복을 가져왔으면서 도난당한 학생의 집합
    intersect = lost_set & reserve_set

    # 여벌 체육복을 가져온 학생이 도난당한 경우에는 여벌 체육복을 본인이 사용
    lost_set -= intersect
    reserve_set -= intersect

    # 여벌 체육복이 있는 경우 무조건 본인의 앞번호 학생에게 먼저 빌려줌을 시도하고
    # 그 후에 뒤에 학생에게 빌려줌을 시도함
    for e in sorted(reserve_set):
        if e - 1 in lost_set:
            lost_set.remove(e - 1)
        elif e + 1 in lost_set:
            lost_set.remove(e + 1)

    return n - len(lost_set)
