from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nums = deque(range(n, 0, -1))
idx = n-1

while len(nums) > 1:
    nums.pop()
    nums.appendleft(nums.pop())

print(nums[0])