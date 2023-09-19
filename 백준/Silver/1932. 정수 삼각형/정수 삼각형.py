import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]
d[0][0] = triangle[0][0]

for depth in range(n):
    if depth == 0:
        continue

    for idx in range(depth+1):
        if idx == 0:
            d[depth][idx] = d[depth-1][0] + triangle[depth][0]
        elif idx == depth:
            d[depth][idx] = d[depth-1][idx-1] + triangle[depth][idx]
        else:
            d[depth][idx] = max(d[depth-1][idx-1] + triangle[depth][idx], d[depth-1][idx] + triangle[depth][idx])

print(max(d[n-1]))