import sys

input = sys.stdin.readline

# 유니온 파인드
def union(network, a, b):
    rootA = find(network, a)
    rootB = find(network, b)
    
    if rootA > rootB:
        rootA, rootB = rootB, rootA
    network[rootB] = rootA

def find(network, x):
    if network[x] == x:
        return x
    network[x] = find(network, network[x])
    return network[x]

T = int(input())

for _ in range(T):
    result = 0
    R, C = map(int, input().split())
    # 2차원 노드들을 1차원으로 표현
    network = [i for i in range(R * C + 1)]
    # 크루스칼을 위한 엣지 배열
    edges = []
    
    # 엣지 구하기
    for i in range(1, R + 1):
        li = list(map(int, input().split()))
        for j, e in enumerate(li, 1):
            start = ((i-1) * C) + j
            end = start + 1
            
            edges.append((e, start, end))
            
    # 엣지 구하기 2
    for i in range(1, R):
        li = list(map(int, input().split()))
        for j, e in enumerate(li, 1):
            start = ((i-1) * C) + j
            end = start + C
            
            edges.append((e, start, end))
    
    # 간선의 비용으로 오름차순 정렬
    edges.sort()
    
    # 크루스칼 알고리즘 돌리기
    count = 0
    for e, start, end in edges:
        if find(network, start) != find(network, end):
            result += e
            count += 1
            union(network, start, end)
        
        if count == (R * C) - 1:
            break
    
    print(result)