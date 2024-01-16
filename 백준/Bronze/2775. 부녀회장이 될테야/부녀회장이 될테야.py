import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0] * (n+1) for _ in range(k+1)]
    dp[0] = list(range(0, n+1))

    for row in range(1, k+1):
        for col in range(1, n+1):
            dp[row][col] = sum(dp[row-1][:col+1])

    print(dp[k][n])