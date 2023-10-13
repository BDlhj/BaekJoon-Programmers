import sys
import heapq
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    num_of_chaps = int(input())
    lens_of_chaps = list(map(int, input().split()))
    heapq.heapify(lens_of_chaps)

    answer = 0
    while len(lens_of_chaps) > 1:
        add_num = heapq.heappop(lens_of_chaps) + heapq.heappop(lens_of_chaps)
        heapq.heappush(lens_of_chaps, add_num)
        answer += add_num
    print(answer)