import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
dp = [-1] * (k+1)
dp[0] = 0

for i in range(1, k+1):
    sub = []
    for j in range(n):
        if i - coins[j] >= 0:
            sub.append(dp[i-coins[j]])

    _min = sys.maxsize
    for v in sub:
        if 0 <= v < _min:
            _min = v

    dp[i] = _min + 1

answer = dp[-1] if dp[-1] < sys.maxsize else -1
print(answer)