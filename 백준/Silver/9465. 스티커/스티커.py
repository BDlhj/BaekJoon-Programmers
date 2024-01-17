import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    answr = 0
    scores = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = scores[0][0]
    dp[1][0] = scores[1][0]

    for col in range(1, n):
        for row in range(2):
            dp[row][col] = max(dp[row][col-1], dp[abs(row-1)][col-1] + scores[row][col])
    
    print(max(dp[0][n-1], dp[1][n-1]))