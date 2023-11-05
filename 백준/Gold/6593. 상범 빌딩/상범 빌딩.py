import sys
from collections import deque
input = sys.stdin.readline

dz = [0, 0, 0, 0, 1, -1]
dy = [0, 1, 0, -1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]

while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break

    building = []
    for _ in range(l):
        building.append([list(input().rstrip()) for _ in range(r)])
        _pass = input()

    q = deque()
    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]

    for h in range(l):
        for row in range(r):
            for col in range(c):
                if building[h][row][col] == 'S':
                    q.append((h, row, col))
                    visited[h][row][col] = 0
                elif building[h][row][col] == 'E':
                    exit_spot = (h, row, col)
    
    while q:
        cz, cy, cx = q.popleft()
        for i in range(6):
            nz = cz + dz[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= nz < l and 0 <= ny < r and 0 <= nx < c) and visited[nz][ny][nx] == -1 and building[nz][ny][nx] != '#':
                q.append((nz, ny, nx))
                visited[nz][ny][nx] = visited[cz][cy][cx] + 1

    if visited[exit_spot[0]][exit_spot[1]][exit_spot[2]] == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {visited[exit_spot[0]][exit_spot[1]][exit_spot[2]]} minute(s).')