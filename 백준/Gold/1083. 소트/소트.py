import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
S = int(input())

for target_num_idx in range(N):
    max_num = 0
    for i in range(target_num_idx, target_num_idx+S+1):
        if i > N-1:
            break
        if nums[i] > max_num:
            max_num = nums[i]
            max_num_idx = i

    for i in range(max_num_idx, target_num_idx, -1):
        nums[i], nums[i-1] = nums[i-1], nums[i]
        S -= 1

    if S <= 0:
        break

print(*nums)

