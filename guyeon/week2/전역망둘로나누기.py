from collections import deque

def solution(n, wires):
    res = 9999
    li = [[] for _ in range(n+1)]
    
    for w in wires:
        li[w[0]].append(w[1])
        li[w[1]].append(w[0])
        
    def bfs(s):
        queue = deque()
        queue.append(s)
        cnt = 1
        visit[s] = 1
        
        while queue:
            node = queue.pop()
            for nn in li[node]:
                if visit[nn] == 0:
                    visit[nn] = 1
                    queue.append(nn)
                    cnt += 1
        return cnt
        
    
    for wire in wires:
        li[wire[0]].remove(wire[1])
        li[wire[1]].remove(wire[0])
        
        visit = [0] * (n+1)
        right = bfs(wire[0])
        visit = [0] * (n+1)
        left = bfs(wire[1])
        
        if abs(right - left) < res:
            res = abs(right - left)
        
        li[wire[0]].append(wire[1])
        li[wire[1]].append(wire[0])
    
    return res