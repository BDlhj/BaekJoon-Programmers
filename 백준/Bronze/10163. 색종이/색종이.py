import sys
input = sys.stdin.readline

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * 1001 for _ in range(1001)]
paper_cnt = {k: 0 for k in range(1, 1001)}

for num in range(1, n+1):
    x, y, width, height = papers[num-1]
    for i in range(height):
        board[y+i][x:x+width] = [num] * width

for row in range(1001):
    for col in range(1001):
        if board[row][col]:
            paper_cnt[board[row][col]] += 1

answer = sorted(list(paper_cnt.items()))
answer = [paper[1] for paper in answer if paper[0] <= n]
print(*answer, sep='\n')
