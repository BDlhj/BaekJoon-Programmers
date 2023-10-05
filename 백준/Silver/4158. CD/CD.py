import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    sg_nums = [int(input()) for _ in range(n)]
    sy_nums = [int(input()) for _ in range(m)]
    answer = 0

    for sg_num in sg_nums:
        idx = bisect_left(sy_nums, sg_num)
        if idx == m:
            idx -= 1
        if sy_nums[idx] == sg_num:
            answer += 1

    print(answer)
