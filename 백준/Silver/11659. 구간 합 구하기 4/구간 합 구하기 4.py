import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]+ list(map(int, input().split()))
nums_sum = [0] * (n+1)
indices = [list(map(int, input().split())) for _ in range(m)]

for i in range(1, n+1):
    nums_sum[i] += nums_sum[i-1] + nums[i]

for idx in indices:
    print(nums_sum[idx[1]] - nums_sum[idx[0]-1])