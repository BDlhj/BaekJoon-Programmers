import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    num_of_houses = 1

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < n and 0 <= nx < n) and not visited[ny][nx] and graph[ny][nx] == '1':
                visited[ny][nx] = True
                q.append((ny, nx))
                num_of_houses += 1
    num_of_houses_list.append(num_of_houses)


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
visited = [[False] * n for _ in range(n)]
num_of_estate = 0
num_of_houses_list = []

for row in range(n):
    for col in range(n):
        if graph[row][col] == '1' and not visited[row][col]:
            num_of_estate += 1
            bfs(row, col)

num_of_houses_list.sort()
print(num_of_estate)
for i in num_of_houses_list:
    print(i)

