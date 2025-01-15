from collections import deque

def solution(n, results):#1:21
    # n번 만큼 반복
    # n번마다 각 n번 노드의 관게를 동기화
    # 2번 노드가 이기는 노드는 2번 상위의 노드들도 이기도록
    # 2번 노드가 지는 노드는 2번의 하위 노드들도 지도록
    
    # 그래프 생성
    graph = [set() for i in range(n+1)]
    
    for match in results:
        graph[match[1]].add(match[0])
        
    # 반복문 n^2 반복 시켜놓고 bfs 돌리면서 순위 동기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            
            queue = deque([j])
            visited = [False] * (n+1)
            visited[j] = True
            
            while queue:
                node = queue.popleft()
                
                for g in graph[node]:
                    if visited[g] == False:
                        visited[g] = True
                        queue.append(g)
                        graph[j].add(g)
    
    #여기부터 순위 구하기
    
    # 이기든 지든 이제 그래프를 양 방향으로 표현
    answer = [0]*(n+1)
    for i in range(1,n+1):
        if len(graph[i]) != 0:
            for gg in graph[i]:
                graph[gg].add(i)
    
    # 노드 n-1개가 있으면 순위가 결정 났다는 것이므로 count
    cnt=0
    for g in graph:
        if len(g) == n-1:
            cnt+=1
            
    return cnt