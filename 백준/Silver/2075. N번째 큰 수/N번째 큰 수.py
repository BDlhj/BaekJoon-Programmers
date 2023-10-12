import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num <= heap[0]:
                continue
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heapq.heappop(heap))