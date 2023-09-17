import sys
input = sys.stdin.readline

# 집 개수
n = int(input())

# 집 색칠 비용
costs = [list(map(int, input().split())) for _ in range(n)]

# d[i][k] : i+1번째 집을 k색으로 칠했을 때의 최소 비용
d = [[0, 0, 0] for _ in range(n)]

# 첫번째 집 색칠 비용 초기화
d[0][0] = costs[0][0]
d[0][1] = costs[0][1]
d[0][2] = costs[0][2]

for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + costs[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + costs[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + costs[i][2]

print(min(d[-1]))