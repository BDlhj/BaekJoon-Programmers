import sys
input = sys.stdin.readline

def find_possible_nums(zero_location):
    row, col = zero_location
    row_square = row//3 * 3
    col_square = col//3 * 3
    return one_to_nine - set([num for num in board[row]]) - set([board[r][col] for r in range(9)]) - set([board[r][c] for r in range(row_square, row_square+3) for c in range(col_square, col_square+3)])

def backtrack(idx):
    possible_nums = find_possible_nums(zero_locations[idx])
    row, col = zero_locations[idx]

    if not possible_nums:
        return False
    
    if idx == len(zero_locations)-1:
        board[row][col] = list(possible_nums)[0]
        for r in board:
            print(*r)
        return True
    
    for num in possible_nums:
        board[row][col] = num
        if not backtrack(idx+1):
            board[row][col] = 0
            continue
        else:
            return True

board = [list(map(int, input().split())) for _ in range(9)]
one_to_nine = set(range(1, 10))
zero_locations = []
for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            zero_locations.append((row, col))

backtrack(0)