import sys
input = sys.stdin.readline

n = int(input())
max_len_nums = []

for second_num in range(1, n+1):
    nums = [n, second_num]
    while True:
        next_num = nums[-2] - nums[-1]
        if next_num >= 0:
            nums.append(next_num)
        else:
            break
    if len(nums) > len(max_len_nums):
        max_len_nums = nums

print(len(max_len_nums))
print(*max_len_nums)