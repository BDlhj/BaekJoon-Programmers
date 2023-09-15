import sys
from itertools import permutations, product
from collections import deque
input = sys.stdin.readline

def rotate(maze, rotate_time):
    tmp = [[0] * 5 for _ in range(5)]
    if rotate_time == 0:
        return maze

    elif rotate_time == 1:
        for row in range(5):
            for col in range(5):
                tmp[row][col] = maze[col][4-row]
        return tmp

    elif rotate_time == 2:
        for row in range(5):
            for col in range(5):
                tmp[row][col] = maze[4-row][4-col]
        return tmp

    elif rotate_time == 3:
        for row in range(5):
            for col in range(5):
                tmp[row][col] = maze[4-col][row]
        return tmp

def bfs(cube):
    visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 0

    while q:
        ch, cy, cx = q.popleft()
        for i in range(6):
            nh = ch + dh[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= nh < 5 and 0 <= ny < 5 and 0 <= nx < 5) and (visited[nh][ny][nx] == -1 and cube[nh][ny][nx]):
                visited[nh][ny][nx] = visited[ch][cy][cx] + 1
                q.append((nh, ny, nx))

    if visited[4][4][4] > 0:
        return visited[4][4][4]
    return sys.maxsize

maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
cube = [[''] * 5 for _ in range(5)]
stack_permus = list(permutations(range(5)))
rotate_products = list(product(range(4), repeat=5))
dy = [0, 1, 0, -1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
min_v = sys.maxsize
done = False

for permu in stack_permus:
    for i in range(5):
        cube[permu[i]] = maze[i]

    # 판 회전하기
    for rotate_product in rotate_products:
        tmp_cube = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            tmp_cube[i] = rotate(cube[i], rotate_product[i])
        
        # 탐색
        if tmp_cube[0][0][0]:
            min_v = min(min_v, bfs(tmp_cube))
            if min_v == 12:
                done = True
                break
    if done:
        break

if min_v == sys.maxsize:
    print(-1)
else:
    print(min_v)