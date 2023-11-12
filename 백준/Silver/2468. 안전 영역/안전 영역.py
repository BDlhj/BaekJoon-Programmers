import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    q = deque([(row, col)])

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < n and 0 <= nx < n) and not visited[ny][nx] and graph[ny][nx] > height:
                visited[ny][nx] = True
                q.append((ny, nx))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
answer = 1

for height in range(1, 100):
    visited = [[False] * n for _ in range(n)]
    num_of_safe_area = 0
    for row in range(n):
        for col in range(n):
            if graph[row][col] > height and not visited[row][col]:
                visited[row][col] = True
                bfs(row, col)
                num_of_safe_area += 1
    
    answer = max(answer, num_of_safe_area)

print(answer)