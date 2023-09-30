import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
sums = set(x+y for x in nums for y in nums)
done = False

for i in range(n-1, -1, -1):
    for j in range(i+1):
        if nums[i] - nums[j] in sums:
            print(nums[i])
            done = True
            break
    if done:
        break