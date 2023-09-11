import sys
input = sys.stdin.readline

t = int(input())
memo = [0] * 11
memo[1], memo[2], memo[3] = 1, 2, 4

for i in range(4, len(memo)):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

for _ in range(t):
    n = int(input())
    print(memo[n])