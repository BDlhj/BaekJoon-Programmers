import sys
import bisect
input = sys.stdin.readline

n = int(input())
values = sorted(list(map(int, input().split())))
cand = sys.maxsize
closest_to_zero = []

for std_v in range(len(values)):
    added_v = bisect.bisect_left(values, -values[std_v])
    if added_v == n:
        added_v -= 1
        
    if values[std_v] == values[added_v]:
        continue
    if cand > abs(values[std_v] + values[added_v]):
        cand = abs(values[std_v] + values[added_v])
        closest_to_zero = [values[std_v], values[added_v]]
        
    if values[std_v] == values[added_v-1]:
        continue
    if cand > abs(values[std_v] + values[added_v-1]):
        cand = abs(values[std_v] + values[added_v-1])
        closest_to_zero = [values[std_v], values[added_v-1]]

print(' '.join(map(str, sorted(closest_to_zero))))