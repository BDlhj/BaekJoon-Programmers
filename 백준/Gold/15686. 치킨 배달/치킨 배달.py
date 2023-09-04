import sys
from itertools import combinations
input = sys.stdin.readline

# 한변의 길이 n, 치킨집 개수 m개
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken_locs = []
house_locs = []
sum_chicken_distances = []

# 집, 치킨집 확인
for row in range(n):
    for col in range(n):
        if city[row][col] == 1:
            house_locs.append((row,col))
        if city[row][col] == 2:
            chicken_locs.append((row,col))

# 치킨집을 m개 고를 수 있는 경우의 수
possible_chicken_combis = list(combinations(chicken_locs, m))

for possible_chicken_combi in possible_chicken_combis:
    sum_chicken_distance = 0
    for house_loc in house_locs:
        chicken_distance = sys.maxsize
        for chicken_loc in possible_chicken_combi:
            chicken_distance = min(chicken_distance, abs(house_loc[0] - chicken_loc[0]) + abs(house_loc[1] - chicken_loc[1]))
        sum_chicken_distance += chicken_distance
    sum_chicken_distances.append(sum_chicken_distance)

print(min(sum_chicken_distances))