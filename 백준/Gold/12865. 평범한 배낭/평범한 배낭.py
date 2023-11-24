import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0] * (k+1) for _ in range(n+1)]
stuff = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for present_weight_of_bag in range(1, k+1):
        weight = stuff[i-1][0]
        value = stuff[i-1][1]

        if present_weight_of_bag < weight:
            bag[i][present_weight_of_bag] = bag[i-1][present_weight_of_bag]
        else:
            bag[i][present_weight_of_bag] = max(value+bag[i-1][present_weight_of_bag-weight], bag[i-1][present_weight_of_bag])

print(bag[n][k])