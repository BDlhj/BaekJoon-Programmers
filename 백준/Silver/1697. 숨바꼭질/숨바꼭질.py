import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([n])
seconds = [-1] * (100001)
seconds[n] = 0
dx = [-1, 1]

while q:
    cx = q.popleft()
    for i in range(3):
        nx = cx * 2 if i == 2 else cx + dx[i]
        if (0 <= nx < 100001) and seconds[nx] == -1:
            seconds[nx] = seconds[cx] + 1
            q.append(nx)


print(seconds[k])