import sys
from collections import deque
input = sys.stdin.readline

n, l = list(map(int, input().split()))
array = list(map(int, input().split()))

min_v = deque()

for i, v in enumerate(array):
    while min_v and min_v[-1][1] > v:
        min_v.pop()
    if min_v and min_v[0][0] < i - l + 1:
        min_v.popleft()
    min_v.append((i, v))
    print(min_v[0][1], end=' ')