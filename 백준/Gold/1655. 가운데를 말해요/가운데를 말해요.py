import sys
import heapq
input = sys.stdin.readline

n = int(input())
min_heap, max_heap = [], []
for _ in range(n):
    num = int(input())
    if len(max_heap) <= len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if min_heap and min_heap[0] < -max_heap[0]:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    print(-max_heap[0])