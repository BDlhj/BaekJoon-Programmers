import sys
input = sys.stdin.readline

n = int(input())
indices = sorted(list(map(int, input().split())) for _ in range(n))
answer = indices[0][1] - indices[0][0]
min_x = indices[0][0]
max_y = indices[0][1]

for i in range(1, len(indices)):
    if indices[i][0] > max_y:
        answer += indices[i][1] - indices[i][0]
        max_y = indices[i][1]

    elif indices[i][1] > max_y:
        answer += indices[i][1] - max_y
        max_y = indices[i][1]
        
print(answer)