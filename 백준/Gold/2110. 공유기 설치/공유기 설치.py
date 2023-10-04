import sys
from bisect import bisect_left
from math import ceil
input = sys.stdin.readline

n, c = map(int, input().split())
locs = [int(input()) for _ in range(n)]
locs.sort()
answer = 0

s, e = 1, ceil((locs[-1] - locs[0]) // (c - 1))

while s <= e:
    mid = (s + e) // 2
    loc = locs[0]
    skip = False
    for _ in range(c-1):
        next_loc_idx = bisect_left(locs, loc+mid)
        if next_loc_idx >= n:
            skip = True
            break
        loc = locs[next_loc_idx]
    if skip:
        e = mid - 1
    else:
        s = mid + 1
        answer = mid

print(answer)