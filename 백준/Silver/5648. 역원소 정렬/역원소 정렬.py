import sys
input = sys.stdin.readline

n, *nums = input().split()

while len(nums) < int(n):
    nums.extend(input().split())

answer = [int(num[::-1]) for num in nums]
answer.sort()
for i in answer:
    print(i)