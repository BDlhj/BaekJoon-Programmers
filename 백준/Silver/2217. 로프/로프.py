import sys
input = sys.stdin.readline

n = int(input())
ws = sorted([int(input()) for _ in range(n)], reverse=True)
max_v = 0

for i, v in enumerate(ws, 1):
    max_v = max(max_v, i * v)

print(max_v)