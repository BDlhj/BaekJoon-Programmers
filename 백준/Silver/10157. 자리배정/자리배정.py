import sys
input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())

if k > c * r:
    print(0)
else:
    board = [[0] * c for _ in range(r)]
    cy, cx = r-1, 0
    direction = 3
    num = 1
    while True:
        if num == k:
            print(cx+1, r-cy)
            break
        board[cy][cx] = num
        num += 1
        if direction == 0:
            if cx == c-1 or board[cy][cx+1]:
                direction = 1
                cy += 1
            else:
                cx += 1
        elif direction == 1:
            if cy == r-1 or board[cy+1][cx]:
                direction = 2
                cx -= 1
            else:
                cy += 1
        elif direction == 2:
            if cx == 0 or board[cy][cx-1]:
                direction = 3
                cy -= 1
            else:
                cx -= 1
        else:
            if cy == 0 or board[cy-1][cx]:
                direction = 0
                cx += 1
            else:
                cy -= 1
