import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
b = deque(map(int, input().split()))
balloons = [(num+1, v) for num, v in enumerate(b)]
idx = 0
while True:
    print(balloons[idx][0], end=' ')
    jump = balloons[idx][1]
    del balloons[idx]
    if not balloons:
        break

    if jump > 0:
        idx = (idx + jump - 1) % len(balloons)
    else:
        idx = (idx + jump) % len(balloons)