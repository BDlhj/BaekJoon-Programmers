from collections import deque


def solution(maps):
    len_r = len(maps)
    len_c = len(maps[0])
    
    dist = [[-1] * len_c for _ in range(len_r)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    dist[0][0] = 1
    queue = deque([(0, 0)])
    
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if (0 <= ny < len_r) and (0 <= nx < len_c):
                if maps[ny][nx] and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    queue.append((ny, nx))
    
    return dist[-1][-1]