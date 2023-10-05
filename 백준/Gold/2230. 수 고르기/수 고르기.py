import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
min_v = sys.maxsize

nums.sort()

for num in nums:
    idx = bisect_left(nums, num+m)
    if idx == n:
        idx -= 1
    if m <= nums[idx] - num < min_v:
        min_v = nums[idx] - num

print(min_v)