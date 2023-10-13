import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

if len(heap) == 1:
    print(0)
else:
    answer = 0
    while len(heap) > 1:
        add_num = heapq.heappop(heap) + heapq.heappop(heap)
        heapq.heappush(heap, add_num)
        answer += add_num
    print(answer)