def solution(routes):
    answer = 0
    # 진입 지점 기준으로 정렬
    routes.sort()

    current_exit_limit = routes[0][1]
    for i, o in routes[1:]:
        # 진출 지점이 현재 진출 지점보다 작으면
        # 현재 진출 지점을 갱신
        current_exit_limit = min(current_exit_limit, o)
        # 진입 지점이 현재 진출 지점보다 작거나 같으면
        # 카메라를 추가하지 않고 넘어감
        if i <= current_exit_limit:
            continue
        # 진입 지점이 현재 진출 지점보다 크면
        # 카메라를 추가하고 현재 진출 지점을 갱신
        current_exit_limit = o
        answer += 1

    # 마지막 차량 집합에 대한 카메라 추가
    answer += 1

    return answer
