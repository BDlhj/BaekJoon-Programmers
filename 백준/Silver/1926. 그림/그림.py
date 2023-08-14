import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cur_area = 0
max_area = 0
cnt = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    area = 1
    q = deque([(y, x)])
    while q:
        cur_y, cur_x = q.popleft()
        for i in range(len(dx)):
            new_y = cur_y + dy[i]
            new_x = cur_x + dx[i]
            if (0 <= new_y < n and 0 <= new_x < m) and (graph[new_y][new_x] and not visited[new_y][new_x]):
                area += 1
                visited[new_y][new_x] = True
                q.append((new_y, new_x))
    return area

for y in range(n):
    for x in range(m):
        if graph[y][x] and not visited[y][x]:
            visited[y][x] = True
            cnt += 1
            cur_area = bfs(y, x)
            max_area = max(max_area, cur_area)

print(cnt)
print(max_area)