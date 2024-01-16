import sys
input = sys.stdin.readline

'''
1번: 넣기 - 2초
2번: 꺼내기 - 1초
최초 땅: B개
최소 시간과 땅 높이(0 <= 높이 <= 256) 출력 | 답 여러 개면 땅의 높이가 가장 높은 것 출력
'''

N, M, B = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]

total_bricks = B + sum([sum(height) for height in heights])
max_height = max([max(height) for height in heights])
time = sys.maxsize
h = -1

if total_bricks // (N * M) > max_height:
    deadline = max_height
else:
    deadline = total_bricks // (N * M)

for i in range(deadline+1):
    cand = 0
    for row in range(N):
        for col in range(M):
            if heights[row][col] > i:
                cand += (2 * (heights[row][col] - i))
            else:
                cand += (i - heights[row][col])

    if cand <= time and i > h:
        time = cand
        h = i
        
print(time, h)