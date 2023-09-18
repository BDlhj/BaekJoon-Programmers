import sys
input = sys.stdin.readline

t = int(input())

d = [[0, 0] for _ in range(45)]
d[0][0], d[0][1] = 1, 0
d[1][0], d[1][1] = 0, 1

for _ in range(t):
    num = int(input())
    for i in range(2, num+1):
        d[i][0], d[i][1] = d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]
    print(d[num][0], d[num][1])