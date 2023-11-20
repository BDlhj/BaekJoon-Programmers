import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
targets = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * (n+1) for _ in range(n+1)]
dp[1][1] = table[0][0]

for row in range(1, n+1):
    for col in range(1, n+1):
        dp[row][col] = dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1] + table[row-1][col-1]

for target in targets:
    answer = dp[target[2]][target[3]] - dp[target[2]][target[1]-1] - dp[target[0]-1][target[3]] + dp[target[0]-1][target[1]-1]
    print(answer)