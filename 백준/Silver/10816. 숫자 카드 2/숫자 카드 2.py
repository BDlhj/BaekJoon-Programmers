import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int, input().split()))
m = int(input())
target_nums = list(map(int, input().split()))

d = defaultdict(int)

for num in nums:
    d[num] += 1

for target_num in target_nums:
    print(d[target_num], end=' ')