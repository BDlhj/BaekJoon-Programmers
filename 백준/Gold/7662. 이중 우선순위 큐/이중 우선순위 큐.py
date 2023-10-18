import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    deleted = [False] * (k+1)
    
    for i in range(k):
        instruction, num = input().rstrip().split()
        if instruction == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
        else:
            if num == '-1':
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
            else:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
        
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
