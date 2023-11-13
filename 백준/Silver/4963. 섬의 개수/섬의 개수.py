import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    q.append((row, col))
    visited[row][col] = True

    while q:
        cy, cx = q.popleft()
        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < h and 0 <= nx < w) and graph[ny][nx] == 1 and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]

    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    dx = [1, 1, 0, -1, -1, -1, 0, 1]

    q = deque()
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for row in range(h):
        for col in range(w):
            if graph[row][col] == 1 and not visited[row][col]:
                bfs(row, col)
                cnt += 1

    print(cnt)