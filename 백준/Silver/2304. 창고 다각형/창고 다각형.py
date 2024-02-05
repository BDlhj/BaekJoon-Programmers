import sys
input = sys.stdin.readline

N = int(input())
pillars = sorted([list(map(int, input().split())) for _ in range(N)])
max_idx = pillars.index(max(pillars, key=lambda x: x[1]))
answer = 0

st_idx = pillars[0][0]
max_height = pillars[0][1]
for i in range(1, max_idx+1):
    if max_height <= pillars[i][1]:
        answer += (pillars[i][0] - st_idx) * max_height
        st_idx = pillars[i][0]
        max_height = pillars[i][1]

st_idx = pillars[-1][0]
max_height = pillars[-1][1]
for i in range(N-1, max_idx-1, -1):
    if max_height <= pillars[i][1]:
        answer += abs(pillars[i][0] - st_idx) * max_height
        st_idx = pillars[i][0]
        max_height = pillars[i][1]

answer += pillars[max_idx][1]

print(answer)

