def solution(tickets):
    # 그래프 생성
    graph = dict()
    answer = []
    # 경로 길이
    path_len = len(tickets) + 1

    # 그래프 생성
    # 출발지를 key로, 도착지와 방문여부를 value로 가지는 딕셔너리 생성
    for t in tickets:
        if graph.get(t[0]):
            graph[t[0]].append([t[1], False])
        else:
            graph[t[0]] = [[t[1], False]]

    # 알파벳 순으로 경로를 정렬
    for t in tickets:
        graph[t[0]].sort()

    # DFS
    def dfs(airport, path):
        # path에 공항 경로 추가
        path.append(airport)

        # path의 길이가 경로 길이와 같다면
        # answer에 path를 복사하고 함수 종료
        if len(path) == path_len:
            answer[:] = path
            return

        # 더 이상 갈 수 있는 경로가 없다면 함수 종료
        if not graph.get(airport):
            return

        # 재귀적인 방식으로 DFS를 구현하여 경로를 찾음
        # 경로를 알파벳 순으로 오름차순 정렬했기 때문에
        # 가장 먼저 나오는 경로를 찾으면 그 경로가 정답임
        for i in range(len(graph[airport])):
            edge = graph[airport][i]
            destination = edge[0]
            # 방문하지 않은 경로라면 방문
            if not edge[1]:
                # 방문 여부를 True로 변경
                edge[1] = True
                # 재귀적으로 DFS를 호출
                dfs(destination, path)
                # 만약 answer가 존재한다면, 즉, 올바른 경로를 찾았다면 함수 종료
                if answer:
                    return
                # answer가 없다면 올바르지 않은 경로이므로
                # 다시 방문하지 않은 경로로 변경하고 path에서 pop
                edge[1] = False
                path.pop()

    dfs("ICN", [])

    return answer
