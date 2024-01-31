import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
board = [[0] * (N+1) for _ in range(M+1)]
board[0][0] = 1
constructing_roads = []
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    if c1 > c2:
        c2, c1 = c1, c2
    if r1 > r2:
        r2, r1 = r1, r2
    constructing_roads.append((c1, r1, c2, r2))

for row in range(M+1):
    for col in range(N+1):
        if row == col == 0:
            continue
        if row == 0 and col != 0:
            if (col-1, row, col, row) not in constructing_roads:
                board[row][col] = board[row][col-1]
        if row != 0 and col == 0:
            if (col, row-1, col, row) not in constructing_roads:
                board[row][col] = board[row-1][col]
        if row >= 1 and col >= 1:
            if (col-1, row, col, row) not in constructing_roads:
                board[row][col] += board[row][col-1]
            if (col, row-1, col, row) not in constructing_roads:
                board[row][col] += board[row-1][col]

print(board[-1][-1])