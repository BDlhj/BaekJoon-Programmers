import sys
from collections import deque
input = sys.stdin.readline

# 테스트 케이스
T = int(input())
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(T):
    # 가로, 세로, 배추 개수
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for row in range(N):
        for col in range(M):
            if graph[row][col] and not visited[row][col]:
                cnt += 1
                q.append((row, col))
                while q:
                    cy, cx = q.popleft()
                    for i in range(4):
                        ny = cy + dy[i]
                        nx = cx + dx[i]
                        if (0 <= ny < N and 0 <= nx < M) and (graph[ny][nx] and not visited[ny][nx]):
                            visited[ny][nx] = 1
                            q.append((ny, nx))
    
    print(cnt)