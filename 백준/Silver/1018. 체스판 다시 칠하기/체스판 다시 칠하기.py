import sys
input = sys.stdin.readline

def count_corner_black(board):
    count = 0
    for row in range(8):
        for col in range(8):
            if row % 2 == 0:
                if col % 2 == 1 and board[row][col] == 'B':
                    count += 1
                elif col % 2 == 0 and board[row][col] == 'W':
                    count += 1
            elif row % 1 == 0:
                if col % 2 == 1 and board[row][col] == 'W':
                    count += 1
                elif col % 2 == 0 and board[row][col] == 'B':
                    count += 1
    return count
            
def count_corner_white(board):
    count = 0
    for row in range(8):
        for col in range(8):
            if row % 2 == 0:
                if col % 2 == 1 and board[row][col] == 'W':
                    count += 1
                elif col % 2 == 0 and board[row][col] == 'B':
                    count += 1
            elif row % 1 == 0:
                if col % 2 == 1 and board[row][col] == 'B':
                    count += 1
                elif col % 2 == 0 and board[row][col] == 'W':
                    count += 1
    return count

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

answer = sys.maxsize
for row in range(N-7):
    for col in range(M-7):
        new = [r[col:col+8] for r in board[row:row+8]]
        answer = min(answer, count_corner_black(new), count_corner_white(new))

print(answer)