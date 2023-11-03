import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

water_q = deque()
water_visited = [[sys.maxsize] * c for _ in range(r)]

hedgehog_q = deque()
hedgehog_visited = [[sys.maxsize] * c for _ in range(r)]

answer = 0
is_done = False

for row in range(r):
    for col in range(c):
        if graph[row][col] == '*':
            water_q.append((row, col))
            water_visited[row][col] = 0
        elif graph[row][col] == 'S':
            hedgehog_q.append((row, col))
            hedgehog_visited[row][col] = 0

while water_q:
    cy, cx = water_q.popleft()
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if (0 <= ny < r and 0 <= nx < c) and water_visited[ny][nx] == sys.maxsize and graph[ny][nx] not in ['D', 'X']:
            water_visited[ny][nx] = water_visited[cy][cx] + 1
            water_q.append((ny, nx))

while hedgehog_q:
    cy, cx = hedgehog_q.popleft()
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if (0 <= ny < r and 0 <= nx < c) and hedgehog_visited[ny][nx] == sys.maxsize and graph[ny][nx] != 'X' and hedgehog_visited[cy][cx] + 1 < water_visited[ny][nx]:
            hedgehog_q.append((ny, nx))
            hedgehog_visited[ny][nx] = hedgehog_visited[cy][cx] + 1
            if graph[ny][nx] == 'D':
                answer = hedgehog_visited[ny][nx]
                is_done = True
                break
    if is_done:
        break

if answer:
    print(answer)
else:
    print('KAKTUS')