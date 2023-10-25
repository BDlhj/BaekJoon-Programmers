import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))
height_diff = []
add_cnt = n - k

for i in range(n-1):
    height_diff.append(heights[i+1] - heights[i])

height_diff.sort()
print(sum(height_diff[:add_cnt]))