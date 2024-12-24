def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)

    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root


def find(parent, x):
    if parent[x] == x:
        return x

    parent[x] = find(parent, parent[x])
    return parent[x]


def solution(n, costs):
    answer = 0
    count = 0
    parent = [i for i in range(n + 1)]

    # cost 순으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # 크루스칼 알고리즘으로 최소비용으로 노드 연결
    # 유니온 파인드 알고리즘 사용
    for e in costs:
        a, b, cost = e

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            count += 1
            answer += cost

        if count == n - 1:
            break

    return answer
