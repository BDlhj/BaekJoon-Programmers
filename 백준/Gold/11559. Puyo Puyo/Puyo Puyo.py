import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    q.append((row, col))
    visited[row][col] = True
    popping_locs.append((row, col))
    cnt = 1
    
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < 12 and 0 <= nx < 6):
                if not visited[ny][nx] and (field[ny][nx] == field[cy][cx]):
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    popping_locs.append((ny, nx))
                    cnt += 1

    # 상하좌우 4개 미만이면 popping_locs에 추가한 거 삭제
    if cnt < 4:
        for i in range(cnt):
            popping_locs.pop()

field = [list(input().rstrip()) for _ in range(12)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
q = deque()
answer = 0

while True:
    visited = [[False] * 6 for _ in range(12)]
    popping_locs = []

    # 없앨 수 있는 뿌요 확인
    for row in range(12):
        for col in range(6):
            if field[row][col] != '.' and not visited[row][col]:
                bfs(row, col)

    # popping_locs에 추가된 거 없으면 break
    if not popping_locs:
        break

    # 뿌요 없애기
    for popping_loc in popping_locs:
        field[popping_loc[0]][popping_loc[1]] = '.'

    # 뿌요 내리기
    for col in range(6):
        dot_row = 0
        dot_exist = False
        for row in range(11, -1, -1):
            if field[row][col] == '.' and not dot_exist:
                dot_row = row
                dot_exist = True
            if field[row][col] != '.' and dot_exist:
                field[row][col], field[dot_row][col] = field[dot_row][col], field[row][col]
                dot_row -= 1

    answer += 1

print(answer)