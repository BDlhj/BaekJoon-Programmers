import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    area = 1
    q = deque([(row, col)])
    visited[row][col] = True

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < m and 0 <= nx < n) and graph[ny][nx] == 0 and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True
                area += 1
                
    return area

m, n, k = map(int, input().split())
rectangles = [list(map(int, input().split())) for _ in range(k)]
graph = [[0] * n for _ in range(m)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
visited = [[False] * n for _ in range(m)]
answer = []

for rectangle in rectangles:
    for row in range(-rectangle[3], -rectangle[1]):
        for col in range(rectangle[0], rectangle[2]):
            graph[row][col] = 1

for row in range(m):
    for col in range(n):
        if graph[row][col] == 0 and not visited[row][col]:
            answer.append(bfs(row, col))

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))