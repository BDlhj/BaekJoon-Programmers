import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
targets = list(map(int, input().split()))
nums = list(range(1, n+1))
crnt_idx = 0
answer = 0

for target in targets:
    direct = abs(nums.index(target) - crnt_idx)
    indirect = len(nums) - nums.index(target) + crnt_idx if target > nums[crnt_idx] else len(nums) - crnt_idx + nums.index(target)
    answer += min(direct, indirect)

    crnt_idx = nums.index(target)
    nums.remove(target)
    if crnt_idx > len(nums) - 1:
        crnt_idx = 0

print(answer)