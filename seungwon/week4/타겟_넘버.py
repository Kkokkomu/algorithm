def dfs(numbers, target, n, val):
    # numbers의 마지막 인덱스에 도달하면
    # 마지막 원소를 더하거나 빼서 target과 같은지 확인
    # 같으면 1을 반환, 아니면 0을 반환
    if n == len(numbers) - 1:
        if val + numbers[n] == target or val - numbers[n] == target:
            return 1
        return 0

    # 재귀적으로 모든 경우의 수를 탐색
    return dfs(numbers, target, n + 1, val + numbers[n]) + dfs(
        numbers, target, n + 1, val - numbers[n]
    )


def solution(numbers, target):
    # dfs를 통해 모든 경우의 수를 탐색
    return dfs(numbers, target, 0, 0)
