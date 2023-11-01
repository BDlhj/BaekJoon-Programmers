import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
answer = 0

for row in range(m):
    for col in range(n):
        if graph[row][col] == 'W':
            continue
        
        q = deque()
        visited = [[0] * n for _ in range(m)]
        q.append((row, col))
        visited[row][col] = 1

        while q:
            cy, cx = q.popleft()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if (0 <= ny < m and 0 <= nx < n) and not visited[ny][nx] and graph[ny][nx] == 'L':
                    q.append((ny, nx))
                    visited[ny][nx] = visited[cy][cx] + 1
        
        partial_max = max([max(row) for row in visited]) - 1
        answer = max(answer, partial_max)
        
print(answer)