import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l = int(input())
    prst = tuple(map(int, input().split()))
    trg = tuple(map(int, input().split()))

    graph = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]
    q = deque([prst])
    visited[prst[0]][prst[1]] = True
    is_done = False
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    dx = [2, 1, -1, -2, -2, -1, 1, 2]

    while q:
        cy, cx = q.popleft()
        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < l and 0 <= nx < l) and (not visited[ny][nx]):
                visited[ny][nx] = True
                graph[ny][nx] = graph[cy][cx] + 1
                if (ny, nx) == trg:
                    is_done = True
                    break
                q.append((ny, nx))
        if is_done:
            break

    print(graph[trg[0]][trg[1]])