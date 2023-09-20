import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))
answer = [times[0]]

for i in range(1, n):
    if times[i][0] >= answer[-1][1]:
        answer.append(times[i])
    
print(len(answer))