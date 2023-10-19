import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    for _ in range(m//10+1):
        nums.extend(list(map(int, input().split())))
    
    max_heap = []
    min_heap = []

    print((m+1)//2)
    for i in range(m):
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -nums[i])
        else:
            heapq.heappush(min_heap, nums[i])
        if max_heap and -max_heap[0] > min_heap[0]:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        if (i+1) % 2 == 1:
            print(min_heap[0], end=' ')
        if i % 20 == 19:
            print()
    print()