import sys
input = sys.stdin.readline

# 세로, 가로
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dp = [[-1] * N for _ in range(M)]

def dfs(row, col):
    if row == M-1 and col == N-1:
        return 1

    if dp[row][col] != -1:
        return dp[row][col]
    
    ways = 0
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        if 0 <= ny < M and 0 <= nx < N:
            if board[ny][nx] < board[row][col]:
                ways += dfs(ny, nx)

    dp[row][col] = ways
    return ways

answer = dfs(0, 0)
print(answer)
