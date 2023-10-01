import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]
max_len = 0

start, end = 1, 2**31 - 1
while start <= end:
    mid = (start+end)//2
    v = 0
    for length in lengths:
        v += length // mid
    if v < n:
        end = mid - 1
    if v >= n:
        start = mid + 1
        max_len = max(max_len, mid)

print(max_len)