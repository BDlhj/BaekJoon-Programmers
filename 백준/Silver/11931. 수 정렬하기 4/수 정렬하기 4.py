import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    merged_list = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[r])
            r += 1
    merged_list += left[l:]
    merged_list += right[r:]
    return merged_list

answer = merge_sort(nums)
for i in answer:
    print(i)