import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
idx_pairs = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}


def recur(dice_idx, top_num):
    top_num_idx = nums[dice_idx].index(top_num)
    bottom_num_idx = idx_pairs[top_num_idx]
    bottom_num = nums[dice_idx][bottom_num_idx]

    new_nums = set(nums[dice_idx]) - {top_num} - {bottom_num}
    if dice_idx == n-1:
        return max(new_nums)
    return max(new_nums) + recur(dice_idx+1, bottom_num)


answer = 0
for num in nums[0]:
    answer = max(answer, recur(0, num))

print(answer)
