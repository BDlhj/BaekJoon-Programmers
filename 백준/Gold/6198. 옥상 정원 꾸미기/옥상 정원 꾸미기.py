import sys
input = sys.stdin.readline

n = int(input())
heights = []
cnt = 0

for _ in range(n):
    height = int(input())
    while heights and height >= heights[-1]:
        heights.pop()
    heights.append(height)
    cnt += (len(heights) - 1)

print(cnt)