import sys
input = sys.stdin.readline

squares = [list(map(int, input().split())) for _ in range(4)]
area = 0

spot_ranges = []
for square in squares:
    spot_ranges.append([(square[0], square[2]), (square[1], square[3])])

for row in range(100):
    for col in range(100):
        for spot_range in spot_ranges:
            y_range = spot_range[1]
            x_range = spot_range[0]
            if y_range[0] <= row < y_range[1] and x_range[0] <= col < x_range[1]:
                area += 1
                break

print(area)