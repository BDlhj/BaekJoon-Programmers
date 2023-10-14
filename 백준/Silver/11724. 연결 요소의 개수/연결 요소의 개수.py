import sys
from collections import deque
input = sys.stdin.readline

def bfs(i):
    q = deque([i])
    visited[i] = True

    while q:
        prst_v = q.popleft()
        for j in range(1, n+1):
            if graph[prst_v][j] and not visited[j]:
                q.append(j)
                visited[j] = True

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
answer = 0
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)