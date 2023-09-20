import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
d = [0] * 1001

for i in nums:
    d[i] = max(d[:i]) + 1

print(max(d))