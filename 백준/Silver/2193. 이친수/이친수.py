import sys
input = sys.stdin.readline

n = int(input())

# d[i][j] : i자리에서 끝자리가 j인 이진수의 개수
d = [[0, 0] for _ in range(n+2)]
d[1][1], d[2][0] = 1, 1

for i in range(2, n+1):
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]

print(sum(d[n]))
