import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

visited = [[False] * M for _ in range(N)]
q = deque()
answer = 0

for row in range(N):
    for col in range(M):
        if board[row][col] == 'I':
            q.append((row, col))
            visited[row][col] = True

while q:
    cy, cx = q.popleft()
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx]:
                if board[ny][nx] != 'X':
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    if board[ny][nx] == 'P':
                        answer += 1

if answer == 0:
    answer = 'TT'

print(answer)