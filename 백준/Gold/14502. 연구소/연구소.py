import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

# 바이러스 퍼뜨리기
def bfs():
    virus_locs_copy = deepcopy(virus_locs)
    visited = [[False] * m for _ in range(n)]
    virus_cnt = len(virus_locs_copy)
    safe_cnt = 0

    while virus_locs_copy:
        cy, cx = virus_locs_copy.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < n and 0 <= nx < m) and not visited[ny][nx] and not board_copy[ny][nx]:
                virus_cnt += 1
                visited[ny][nx] = True
                board_copy[ny][nx] = 2
                virus_locs_copy.append((ny, nx))

    safe_cnt = spaces_num - virus_cnt - (wall_cnt+3)
    return safe_cnt

# 세로 크기, 가로 크기
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
spaces_num = n * m
wall_cnt = 0
max_safe = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 빈 공간들의 좌표
empty_locs = []

# 바이러스 좌표
virus_locs = deque()

for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            empty_locs.append((r, c))
        if board[r][c] == 1:
            wall_cnt += 1
        if board[r][c] == 2:
            virus_locs.append((r, c))

# 벽을 세울 빈 공간 세 개의 조합
empty_combis = list(combinations(empty_locs, 3))

for empty_combi in empty_combis:
    board_copy = deepcopy(board)

    for loc in empty_combi:
        board_copy[loc[0]][loc[1]] = 1

    safe_cnt = bfs()
    max_safe = max(max_safe, safe_cnt)

print(max_safe)
