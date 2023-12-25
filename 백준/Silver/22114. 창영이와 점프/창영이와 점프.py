import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

dp = [[0] * n for _ in range(2)]
dp[0][0], dp[1][0] = 1, 1

for i in range(n-1):
    if l[i] <= k:
        dp[0][i+1] = dp[0][i] + 1
        dp[1][i+1] = dp[1][i] + 1
    else:
        dp[0][i+1] = 1
        dp[1][i+1] = dp[0][i] + 1

answer = max(map(max, dp))
print(answer)