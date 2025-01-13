from collections import deque


def solution(n, edge):
    # 인접 리스트 생성
    adj_li = [[] for _ in range(n + 1)]
    # 방문 여부
    is_visited = [False for _ in range(n + 1)]
    # 거리별 노드 개수
    count_dict = dict()

    # 인접 리스트 생성
    for a, b in edge:
        adj_li[a].append(b)
        adj_li[b].append(a)

    # BFS
    dq = deque()
    dq.append((1, 1))
    while dq:
        node, count = dq.popleft()
        if is_visited[node]:
            continue
        is_visited[node] = True

        # 거리별 노드 개수 카운트
        if count_dict.get(count):
            count_dict[count] += 1
        else:
            count_dict[count] = 1

        for next_node in adj_li[node]:
            dq.append((next_node, count + 1))

    # 가장 먼 노드의 개수 반환
    return count_dict[max(count_dict.keys())]
