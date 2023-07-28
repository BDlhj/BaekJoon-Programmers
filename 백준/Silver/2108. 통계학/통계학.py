import sys
import collections

input=sys.stdin.readline

n = int(input())
nums = []
modes = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()
nums_items = list(dict(collections.Counter(nums)).items())
nums_items.sort(key=lambda x: (x[1], x[0]))

for nums_item in nums_items:
    if nums_item[1] == nums_items[-1][1]:
        modes.append(nums_item)

mean = round(sum(nums) / len(nums))
median = nums[len(nums) // 2]
mode = modes[1][0] if len(modes) > 1 else modes[-1][0]
scope = max(nums) - min(nums)

print(mean)
print(median)
print(mode)
print(scope)