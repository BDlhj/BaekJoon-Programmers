import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
max_length = max(n, m)
answer = 1

for row in range(n):
    for col in range(m):
        for length in range(1, max_length):
            if row+length < n and col+length < m:
                if board[row][col] == board[row+length][col] == board[row][col+length] == board[row+length][col+length]:
                    answer = max(answer, (length+1)**2)

print(answer)