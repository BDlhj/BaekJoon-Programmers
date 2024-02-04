import sys
input = sys.stdin.readline

paper_cnt = int(input())
locations = [list(map(int, input().split())) for _ in range(paper_cnt)]
answer = 0

for row in range(100):
    for col in range(100):
        
        for loc in locations:
            if loc[1] <= col < loc[1]+10 and loc[0] <= row < loc[0]+10:
                answer += 1
                break

print(answer)