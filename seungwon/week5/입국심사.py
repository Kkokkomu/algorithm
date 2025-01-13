def solution(n, times):
    answer = 0
    times.sort()
    # 최솟값
    left = times[0]
    # 최대값
    right = times[0] * n

    # 이분탐색
    while left <= right:
        mid = (left + right) // 2

        tmp = 0
        # mid 시간동안 심사할 수 있는 사람 수
        for t in times:
            tmp += mid // t
            # n명을 초과하여 심사할 수 있으면 break
            if tmp > n:
                break

        # n명 이상을 심사할 수 있는 경우
        # 시간을 줄여본다
        # tmp == n인 경우에도, 더 최소 시간을 찾기 위해 right를 줄여본다
        if tmp >= n:
            answer = mid
            right = mid - 1
        # n명을 심사할 수 없는 경우
        # 시간을 늘려본다
        else:
            left = mid + 1

    return answer
