import sys

n = int(sys.stdin.readline())
nums = [0] * 10001

for _ in range(n):
    nums[int(sys.stdin.readline())] += 1

for i in range(10001):
    if nums[i]:
        for _ in range(nums[i]):
            print(i)