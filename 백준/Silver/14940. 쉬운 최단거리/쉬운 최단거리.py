import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dist = [[-1] * M for _ in range(N)]
q = deque()

for row in range(N):
    for col in range(M):
        if board[row][col] == 2:
            loc = (row, col)
            dist[row][col] = 0
        elif board[row][col] == 0:
            dist[row][col] = 0

q.append(loc)
while q:
    cy, cx = q.popleft()
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if dist[ny][nx] == -1:
                q.append((ny, nx))
                dist[ny][nx] = dist[cy][cx] + 1

for i in dist:
    print(*i)