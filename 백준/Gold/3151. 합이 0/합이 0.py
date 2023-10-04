import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
levels = list(map(int, input().split()))
levels.sort()
answer = 0

for i in range(n):
    for j in range(i+1, n):
        target = -(levels[i] + levels[j])
        answer += (bisect_right(levels, target, j+1, n) - bisect_left(levels, target, j+1, n))

print(answer)