import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if matrix[v][i] == 1 and visited[i] == 0:            
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        cur_v = q.popleft()
        print(cur_v, end=' ')
        for i in range(1, n+1):
            if matrix[cur_v][i] and  not visited[i]:
                visited[i] = 1
                q.append(i)

n, m, v = list(map(int, input().split()))
matrix = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

# dfs
dfs(v)
print()

# bfs
visited = [0] * (n+1)
bfs(v)