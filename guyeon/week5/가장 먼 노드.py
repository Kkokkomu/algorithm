from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for i in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    visited = [-1] * (n+1)
    visited[1] = 0
    
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        
        for n in graph[node]:
            if visited[n] == -1:
                visited[n] = visited[node] + 1
                queue.append(n)
                
    
    # print(graph)
    # print(visited)
    
    return visited.count(max(visited))