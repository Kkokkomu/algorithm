def dfs(i, computers, is_visited):
    # 이미 방문한 컴퓨터라면 종료
    if is_visited[i]:
        return

    # 방문한 컴퓨터로 표시
    is_visited[i] = True
    # 현재 컴퓨터와 연결된 컴퓨터를 모두 방문
    for j in range(len(computers[i])):
        if computers[i][j]:
            dfs(j, computers, is_visited)


def solution(n, computers):
    answer = 0
    # 방문 여부를 저장하는 리스트
    is_visited = [False] * n

    # 모든 컴퓨터를 방문할 때까지 dfs를 실행
    for i in range(len(computers)):
        # 모든 컴퓨터를 돌며 방문하지 않은 컴퓨터라면 dfs 실행
        if not is_visited[i]:
            answer += 1
            dfs(i, computers, is_visited)

    return answer
