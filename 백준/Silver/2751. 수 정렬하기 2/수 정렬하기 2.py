import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

for num in sorted(nums):
    print(num)