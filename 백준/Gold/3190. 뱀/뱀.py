import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 보드 크기
n = int(input())

# 사과 개수
k = int(input())

# 사과 위치
apple_locs = [list(map(int, input().split())) for _ in range(k)]

# 방향 변환 횟수
l = int(input())

# 방향 변환 정보(L: 왼쪽, D: 오른쪽)
l_infos = [input().rstrip().split() for _ in range(l)]
turn_times = [int(turn_time[0]) for turn_time in l_infos]

board = [[0] * n for _ in range(n)]
time = 0

# 사과 위치 표시(1)
for apple_loc in apple_locs:
    board[apple_loc[0]-1][apple_loc[1]-1] = 1

# 뱀 위치 담은 덱
snake = deque()

# 동 남 서 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
game_over = False


# 머리가 row, col에서 d 방향을 향하고 있을 때 움직이는 함수
def move(r, c, d):
    global time, game_over
        
    if (r < 0 or r >= n) or (c < 0 or c >= n):
        game_over = True
        return

    if (r, c) in snake:
        game_over = True
        return

    snake.appendleft((r, c))

    if board[r][c] == 0:
        y, x = snake.pop()
        board[y][x] = 0
    
    board[r][c] = -1

    if time in turn_times:
        idx = turn_times.index(time)
        d = (d+1) % 4 if l_infos[idx][1] == 'D' else (d-1) % 4
    time += 1

    move(r+dy[d], c+dx[d], d)

board[0][0] = -1
move(0, 0, 0)
print(time)