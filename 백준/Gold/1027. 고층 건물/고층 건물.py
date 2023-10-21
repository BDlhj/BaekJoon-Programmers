import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
answer = 0

for i in range(n): # 기준 높이 인덱스
    cnt = 0
    for j in range(n): # 비교하는 높이 인덱스
        if i == j:
            continue
        possible = True
        if i > j:
            d = (heights[i] - heights[j]) / (i - j)
            for k in range(j+1, i):
                if heights[k] >= heights[j] + (k-j) * d:
                    possible = False
                    break
        if j > i:
            d = (heights[j] - heights[i]) / (j - i)
            for k in range(i+1, j):
                if heights[k] >= heights[i] + (k-i) * d:
                    possible = False
                    break
        if possible:
            cnt += 1
    answer = max(answer, cnt)
print(answer)