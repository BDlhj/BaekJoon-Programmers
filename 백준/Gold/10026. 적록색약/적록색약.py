import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited_1 = [[False] * N for _ in range(N)]
visited_2 = [[False] * N for _ in range(N)]
q_1 = deque()
q_2 = deque()
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
cnt_1 = 0
cnt_2 = 0

for row in range(N):
    for col in range(N):
        if not visited_1[row][col]:
            q_1.append((row, col))
            visited_1[row][col] = True
            cnt_1 += 1
        while q_1:
            cy, cx = q_1.popleft()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if (0 <= ny < N and 0 <= nx < N) and (graph[ny][nx] == graph[cy][cx] and not visited_1[ny][nx]):
                    visited_1[ny][nx] = True
                    q_1.append((ny, nx))

        if not visited_2[row][col]:
            q_2.append((row, col))
            visited_2[row][col] = True
            cnt_2 += 1
        while q_2:
            cy, cx = q_2.popleft()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if ((0 <= ny < N and 0 <= nx < N) and not visited_2[ny][nx]):
                    if (graph[ny][nx] == graph[cy][cx]) or ((graph[ny][nx] != graph[cy][cx]) and (graph[ny][nx] in ['R', 'G'] and graph[cy][cx] in ['R', 'G'])):
                        visited_2[ny][nx] = True
                        q_2.append((ny, nx))

print(cnt_1, cnt_2)