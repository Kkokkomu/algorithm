def solution(n, results):
    answer = 0
    # 0으로 초기화된 2차원 그래프 생성
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    # a가 b를 이겼을 때, graph[a][b] = 1, graph[b][a] = -1
    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1

    # 플로이드 와샬 알고리즘
    # a가 b를 이기고, b가 c를 이겼을 때, a가 c를 이긴다
    # x가 y에게 패배하고, y가 z에게 패배했을 때, x가 z에게 패배한다
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if graph[i][k] and graph[i][k] == graph[k][j]:
                    graph[i][j] = graph[i][k]

    # 0이 2개인 경우, 즉, index를 편하게 맞추기 위해 넣은 0번째 인덱스와 자기 자신 index를 제외하고 모두 값이 있는 경우
    # 즉, 다른 모든 노드들과의 승패 결과를 알 수 있는 경우 answer += 1
    for g in graph:
        if g.count(0) == 2:
            answer += 1

    return answer
