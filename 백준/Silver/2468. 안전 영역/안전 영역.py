import sys
from collections import deque
input = sys.stdin.readline

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(height):
    while qu:
        r,c = qu.popleft()
        for i in range(4):
            row = r+dr[i]
            col = c+dc[i]
            if 0 <= row < N and 0 <= col < N:
                if not visited[row][col] and arr[row][col] > height:
                    visited[row][col] = True
                    qu.append((row,col))

N = int(input().strip())
arr = []
qu = deque()
max_n = 0
max_cnt = 0
for _ in range(N):
    row = list(map(int,input().strip().split()))
    max_row = max(row)
    if max_n < max_row:
        max_n = max_row
    arr.append(row)

for i in range(0,max_n):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > i:
                visited[r][c] = True
                qu.append((r,c))
                bfs(i)
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)