import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
answer = 0

nums.sort()
s_i, e_i = 0, n-1
while s_i < e_i:
    if nums[s_i] + nums[e_i] == x:
        answer += 1
        e_i -= 1
    if nums[s_i] + nums[e_i] > x:
        e_i -= 1
    if nums[s_i] + nums[e_i] < x:
        s_i += 1

print(answer)