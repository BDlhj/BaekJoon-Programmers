import sys
input = sys.stdin.readline

x, y = map(int, input().split())
answer = (x + y) if y < x else (y % x)
print(answer)