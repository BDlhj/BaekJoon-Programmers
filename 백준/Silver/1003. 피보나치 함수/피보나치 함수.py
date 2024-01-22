import sys
input = sys.stdin.readline

memo = {
    0: [1, 0],
    1: [0, 1]
}

for num in range(2, 41):
    memo[num] = list(map(lambda x, y: x+y, memo[num-1], memo[num-2]))

t = int(input())
for _ in range(t):
    n = int(input())
    print(*memo[n])