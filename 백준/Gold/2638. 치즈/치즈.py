import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
answer = 0

while True:
    is_done = True
    q = deque()
    visited = [[False] * m for _ in range(n)]
    contact_num = [[0] * m for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = True

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < n and 0 <= nx < m):
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                if graph[ny][nx] == 1:
                    is_done = False
                    contact_num[ny][nx] += 1
        
    for row in range(n):
        for col in range(m):
            if contact_num[row][col] >= 2:
                graph[row][col] = 0

    if is_done:
        break
    answer += 1

print(answer)