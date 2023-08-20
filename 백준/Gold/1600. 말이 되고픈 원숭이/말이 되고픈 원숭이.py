import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

def bfs():
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        cy, cx, hor_time = q.popleft()
        if cy == h-1 and cx == w-1:
            return visited[cy][cx][hor_time] - 1
        for i in range(4):
            ny = cy + mon_mov[i][0]
            nx = cx + mon_mov[i][1]
            if (0 <= ny < h and 0 <= nx < w) and (not graph[ny][nx] and not visited[ny][nx][hor_time]):
                q.append((ny, nx, hor_time))
                visited[ny][nx][hor_time] = visited[cy][cx][hor_time] + 1
        if hor_time < k:
            for i in range(8):
                ny = cy + hor_mov[i][0]
                nx = cx + hor_mov[i][1]
                if (0 <= ny < h and 0 <= nx < w) and (not graph[ny][nx] and not visited[ny][nx][hor_time+1]):
                    q.append((ny, nx, hor_time+1))
                    visited[ny][nx][hor_time+1] = visited[cy][cx][hor_time] + 1

    return -1

w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
mon_mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]
hor_mov = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
q = deque()

print(bfs())