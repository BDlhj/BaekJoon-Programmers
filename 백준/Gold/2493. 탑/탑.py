import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
prev_heights = []
answer = []
for i in range(n):    
    while prev_heights:
        if heights[i] >= prev_heights[-1][1]:
            prev_heights.pop()
        else:
            answer.append(prev_heights[-1][0] + 1)
            break
    if not prev_heights:
        answer.append(0)
    prev_heights.append([i, heights[i]])

print(" ".join(map(str, answer)))