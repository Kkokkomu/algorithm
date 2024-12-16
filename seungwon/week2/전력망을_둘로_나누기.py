def union(parent, cnt, v1, v2):
    v1_root = find(parent, v1)
    v2_root = find(parent, v2)
    if v1_root != v2_root:
        parent[v1_root] = v2_root
        cnt[v2_root] += cnt[v1_root]


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def solution(n, wires):
    answer = 100

    # 전선 하나를 제외하고 모든 전선을 이어서 트리를 2개 만들고 트리의 개수 차이를 확인
    # 이 과정을 모든 전선에 대해 반복하여 완전탐색함
    for i in range(len(wires)):
        parent = [j for j in range(n + 1)]
        cnt = [1 for _ in range(n + 1)]
        t1_idx = 0
        t2_idx = 0

        for idx, w in enumerate(wires):
            v1, v2 = w

            # 각 반복마다 전선을 하나씩 자름
            if idx == i:
                # 잘라진 전선의 양쪽 노드를 저장
                t1_idx = v1
                t2_idx = v2
                continue

            # 유니온 파인드
            union(parent, cnt, v1, v2)

        gap = abs(cnt[find(parent, t1_idx)] - cnt[find(parent, t2_idx)])
        answer = min(answer, gap)

    return answer
