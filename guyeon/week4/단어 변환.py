from collections import deque

def diffCnt(a, b):
    cnt=0
    for aa, bb in zip(a, b):
        if aa != bb:
            cnt+=1
    return cnt

def solution(begin, target, words): #0105~0140
    if target not in words:
        return 0
    
    words.append(begin)
    words.append(target)
    
    # 방문 배열 생성
    visited = [-1] * (len(words))
    
    # 인접리스트 생성
    li = [[] for i in range(len(words))]
    for i in range(len(words)):
        for j in range(i, len(words)):
            if diffCnt(words[i] , words[j]) == 1:
                li[i].append(j)
                li[j].append(i)
    
    # begin 부터 bfs
    queue = deque([len(words)-2])
    visited[len(words)-2] = 0
    
    while queue:
        crr = queue.popleft()
        
        for ll in li[crr]:
            if visited[ll] == -1:
                visited[ll] = visited[crr] + 1
                queue.append(ll)
    
    return visited[-1]