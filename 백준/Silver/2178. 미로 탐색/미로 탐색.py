import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
q = deque([(0, 0)])

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < n and 0 <= nx < m) and (graph[ny][nx] == 1):
            if ny == 0 and nx == 0:
                continue
            graph[ny][nx] = graph[y][x] + 1
            q.append((ny, nx))

print(graph[n-1][m-1])