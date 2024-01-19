import sys
input = sys.stdin.readline

n = int(input())
dp = [4] * (n+1)
dp[0], dp[1] = 0, 1

for num in range(2, n+1):
    if (num ** 0.5) % 1 == 0:
        dp[num] = 1
    else:
        i = 1
        while i ** 2 < num:
            dp[num] = min(dp[num], dp[num - i**2]+1)
            i += 1

print(dp[-1])