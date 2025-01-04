from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(maps):
    lx = len(maps[0]) # 맵 가로 길이
    ly = len(maps) # 맵 세로 길이
    
    queue = deque([(0, 0)]) # BFS

    while queue:
        x,y = queue.popleft()
        

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<lx and 0<=ny<ly: # 변위를 더한 좌표가 경계값을 벋어나지 않느지 검사, 그리고 벽이 아닌지 검사
                if maps[ny][nx] == 1: # 들린적이 없거나 벽이 아닐 경우에 방문
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((nx, ny))
    
    if maps[ly-1][lx-1] == 1: # 도달하지 못했다면 -1
        return -1
    else:
        return maps[ly-1][lx-1] # 도달했다면 값 반환
                
