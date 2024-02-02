import sys
input = sys.stdin.readline


def check_rows():
    states = [sum(row) for row in visited]
    return states.count(5)

def check_cols():
    states = [sum(col) for col in zip(*visited)]
    return states.count(5)

def check_diagonals():
    first = sum([visited[i][i] for i in range(5)])
    second = sum([visited[i][4-i] for i in range(5)])
    return (first == 5) + (second == 5)

def check_bingo():
    for row in range(5):
        for col in range(5):
            if board[row][col] == num:
                visited[row][col] = True
                if check_rows() + check_cols() + check_diagonals() >= 3:
                    return True
                return False

board = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]
answer = [num for row in answer for num in row]

visited = [[False] * 5 for _ in range(5)]
cnt = 0

for num in answer:
    cnt += 1
    if check_bingo():
        break

print(cnt)