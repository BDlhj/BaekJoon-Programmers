import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    start_count = end_count = 0
    circles = [list(map(int, input().split())) for _ in range(n)]

    for circle in circles:
        cx, cy, r = circle
        if math.sqrt((cx - x1)**2 + (cy-y1)**2) < r and math.sqrt((cx - x2)**2 + (cy-y2)**2) < r:
            continue
        elif math.sqrt((cx - x1)**2 + (cy-y1)**2) < r:
            start_count += 1
        elif math.sqrt((cx - x2)**2 + (cy-y2)**2) < r:
            end_count += 1

    print(start_count + end_count)
