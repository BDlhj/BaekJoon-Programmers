import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]
dp[1] = list(range(31))

for row in range(2, 31):
    for col in range(1, 31):
        dp[row][col] = sum(dp[row-1][:col])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])