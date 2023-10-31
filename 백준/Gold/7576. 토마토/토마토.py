import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for row in range(n):
    for col in range(m):
        if graph[row][col] == 1:
            visited[row][col] = True
            q.append((row, col))

while q:
    cy, cx = q.popleft()
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if (0 <= ny < n and 0 <= nx < m) and not visited[ny][nx] and graph[ny][nx] == 0:
            q.append((ny, nx))
            visited[ny][nx] = True
            graph[ny][nx] = graph[cy][cx] + 1

is_possible = True
max_dist = 0
for row in range(n):
    for col in range(m):
        if graph[row][col] == 0:
            is_possible = False
            break
        max_dist = max(max_dist, graph[row][col] - 1)
    if not is_possible:
        break

if is_possible:
    print(max_dist)
else:
    print(-1)
