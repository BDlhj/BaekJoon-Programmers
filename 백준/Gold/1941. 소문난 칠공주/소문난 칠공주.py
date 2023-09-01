import sys
from collections import deque
input = sys.stdin.readline

def check():
    q = deque()
    visited = [[False] * 5 for _ in range(5)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    cnt = 0

    for row in range(5):
        for col in range(5):
            if is_used[row][col]:
                q.append((row, col))
                visited[row][col] = True
                cnt += 1
                break
        if q:
            break
    
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < 5 and 0 <= nx < 5) and (not visited[ny][nx] and is_used[ny][nx]):
                visited[ny][nx] = True
                q.append((ny, nx))
                cnt += 1

    return cnt == 7

def backtrack(k, s_idx):
    global answer

    if k == member_num:
        if check():
            answer += 1
        return
    
    for i in range(s_idx, std_num):
        if not is_used[i//5][i%5]:
            permu[k] = graph[i//5][i%5]
            if permu.count('Y') >= 4:
                permu[k] = graph[i//5][i%5]
                continue
            is_used[i//5][i%5] = True
            backtrack(k+1, i+1)
            is_used[i//5][i%5] = False
    permu[k] = ''

graph = [list(input().rstrip()) for _ in range(5)]
std_num = 25
member_num = 7
permu = [''] * member_num
is_used = [[False] * 5 for _ in range(5)]
possible_members = []
answer = 0

backtrack(0, 0)
print(answer)
