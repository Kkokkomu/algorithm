from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(rectangle, characterX, characterY, itemX, itemY): #0219~0317
    graph = [[-1 for i in range(102)] for i in range(102)] # ㅁ 으로 인식되는걸 방지하기 위해 좌표를 2배로 확대함, 일단 전부 -1로 초기화
    
    for r in rectangle: # 직사각형 순회
        x1,y1,x2,y2 = map(lambda x : x*2, r) # 직사각형 좌표도 2배 확대
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2: # 도형 안에 있으면 0으로 초기화
                    graph[y][x] = 0
                elif graph[y][x] != 0: # 다른 도형안에 속해있지 않다면 
                    graph[y][x] = 1 # 1로 초기화
    # 도형 안은 0, 도형밖은 -1, 경로만 1로 남은

    # 이후에는 그냥 1 따라서 bfs하면 끝

    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    
    queue = deque([(cy, cx)])
    while queue:
        y, x = queue.popleft()
        if y == iy and x == ix:
            return graph[iy][ix]//2 # 좌표를 2배 확대했으므로 반환은 2나누기
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 102 and 0 <= ny <102:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((ny, nx))
    return 0
