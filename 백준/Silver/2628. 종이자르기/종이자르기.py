import sys
input = sys.stdin.readline

width, height = map(int, input().split())
num_of_lines = int(input())
lines = [list(map(int, input().split())) for _ in range(num_of_lines)]

widths = [0]
heights = [0]

for line in lines:
    if line[0] == 0:
        heights.append(line[1])
    else:
        widths.append(line[1])

widths.append(width)
heights.append(height)

widths.sort()
heights.sort()

max_width = 0
max_height = 0
for i in range(1, len(widths)):
    for j in range(1, len(heights)):
        max_width = max((widths[i] - widths[i-1]), max_width)
        max_height = max((heights[j] - heights[j-1]), max_height)

print(max_width * max_height)