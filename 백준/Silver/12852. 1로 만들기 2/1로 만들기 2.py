import sys
input = sys.stdin.readline

n = int(input())
d = [[0, []] for _ in range(n+3)]
d[1], d[2], d[3] = [0, [1]], [1, [1, 2]], [1, [1, 3]]

for i in range(4, n+1):
    d[i][0] = d[i-1][0] + 1
    d[i][1] = d[i-1][1] + [i]
    if i % 2 == 0:
        d[i][0] = min(d[i][0], d[i//2][0] + 1)
        if d[i][0] == d[i//2][0] + 1:
            d[i][1] = d[i//2][1] + [i]
    if i % 3 == 0:
        d[i][0] = min(d[i][0], d[i//3][0] + 1)
        if d[i][0] == d[i//3][0] + 1:
            d[i][1] = d[i//3][1] + [i]

print(d[n][0])
for i in d[n][1][::-1]:
    print(i, end=' ')