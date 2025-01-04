def solution(n, computers): # 2020~2041
    visited = [False] * n
    
    def dfs(n):
        visited[n] = True
        for i, n in enumerate(computers[n]):
            if n == 1 and visited[i] == False:
                dfs(i)
    
    cnt=0
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            cnt+=1
    
    return cnt