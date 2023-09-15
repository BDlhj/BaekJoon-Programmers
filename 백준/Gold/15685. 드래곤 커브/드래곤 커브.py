import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * 105 for _ in range(105)]
cnt = 0

for _ in range(n):
    x, y, d, g = map(int, input().split())
    v = [d]
    board[y][x] = 1

    for _ in range(g):
        v_size = len(v)
        for j in range(v_size-1, -1, -1):
            v.append((v[j] + 1) % 4)

    for dir in v:
        if dir == 0:
            x += 1
        elif dir == 1:
            y -= 1
        elif dir == 2:
            x -= 1
        elif dir == 3:
            y += 1
        board[y][x] = 1

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            cnt += 1

print(cnt)