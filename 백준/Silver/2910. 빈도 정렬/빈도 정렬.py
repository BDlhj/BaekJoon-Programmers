import sys
from collections import defaultdict
input = sys.stdin.readline

n, c = map(int, input().split())
nums = list(map(int, input().split()))
nums_dict = defaultdict(int)

for num in nums:
    nums_dict[num] += 1

nums_dict_items = sorted(list(nums_dict.items()), key=lambda x: x[1], reverse=True)

for nums_dict_item in nums_dict_items:
    for _ in range(nums_dict_item[1]):
        print(nums_dict_item[0], end=' ')