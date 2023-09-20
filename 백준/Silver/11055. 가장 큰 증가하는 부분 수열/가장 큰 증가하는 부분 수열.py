import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
d = nums[:]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and d[i] < d[j] + nums[i]:
            d[i] = d[j] + nums[i]

print(max(d))