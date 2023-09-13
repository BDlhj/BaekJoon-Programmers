import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

for i in sorted(nums):
    print(i)