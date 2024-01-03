import sys
input = sys.stdin.readline

n = int(input())
ais = list(map(int, input().split()))
dp = [sys.maxsize] * n
dp[0] = 0

for i in range(n):
    for j in range(1, ais[i]+1):
        if i + j < n:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

if dp[-1] == sys.maxsize:
    print(-1)
else:
    print(dp[-1])