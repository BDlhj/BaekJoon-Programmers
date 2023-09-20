import sys
input = sys.stdin.readline

def initialize(n):
    d[1][1] = scores[1]
    if n >= 2:
        d[2][1], d[2][2] = scores[2], d[1][1]+scores[2]

n = int(input())
scores = [0] + [int(input()) for _ in range(n)]

# d[i][j] : i번째 계단에 연속해서 j개의 계단을 밟고 올랐을 때의 최대값
d = [[0, 0, 0] for _ in range(301)]
initialize(n)

for i in range(3, n+1):
    d[i][1] = max(d[i-2][1] + scores[i], d[i-2][2] + scores[i])
    d[i][2] = d[i-1][1] + scores[i]

print(max(d[n]))