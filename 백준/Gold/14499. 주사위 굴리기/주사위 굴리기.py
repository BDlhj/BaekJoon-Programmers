import sys
input = sys.stdin.readline

def move_up(row, col):
    if row == 0:
        return row, col
    
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    
    if board[row-1][col] == 0:
        board[row-1][col] = dice[3][1]
    else:
        dice[3][1] = board[row-1][col]
        board[row-1][col] = 0
    answer.append(dice[1][1])
    return row-1, col
    
def move_down(row, col):
    if row == n-1:
        return row, col
    
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    
    if board[row+1][col] == 0:
        board[row+1][col] = dice[3][1]
    else:
        dice[3][1] = board[row+1][col]
        board[row+1][col] = 0
    answer.append(dice[1][1])
    return row+1, col

def move_right(row, col):
    if col == m-1:
        return row, col

    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    
    if board[row][col+1] == 0:
        board[row][col+1] = dice[3][1]
    else:
        dice[3][1] = board[row][col+1]
        board[row][col+1] = 0
    answer.append(dice[1][1])
    return row, col+1

def move_left(row, col):
    if col == 0:
        return row, col

    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    
    if board[row][col-1] == 0:
        board[row][col-1] = dice[3][1]
    else:
        dice[3][1] = board[row][col-1]
        board[row][col-1] = 0
    answer.append(dice[1][1])
    return row, col-1

# 세로, 가로, x좌표, y좌표, 명령 개수
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
instructions = list(map(int, input().split()))
dice = [[-1] * 3 for _ in range(4)]
dice[0][1], dice[1][0], dice[1][1], dice[1][2], dice[2][1], dice[3][1] = [0] * 6
instructions_funcs = {1: move_right, 2: move_left, 3: move_up, 4: move_down}
answer = []

for num in instructions:
    x, y = instructions_funcs[num](x, y)

for i in answer:
    print(i)