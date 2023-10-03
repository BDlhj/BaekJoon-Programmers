import sys
import bisect
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
mix_v = sys.maxsize

for value in values:
    opposite_value_idx = bisect.bisect_left(values, -value)
    if opposite_value_idx == n:
        opposite_value_idx -= 1

    if abs(value + values[opposite_value_idx]) < mix_v and value != values[opposite_value_idx]:
        mix_v = abs(value + values[opposite_value_idx])
        answer = sorted([value, values[opposite_value_idx]])

    if abs(value + values[opposite_value_idx-1]) < mix_v and value != values[opposite_value_idx-1]:
        mix_v = abs(value + values[opposite_value_idx-1])
        answer = sorted([value, values[opposite_value_idx-1]])

print(' '.join(map(str, answer)))
