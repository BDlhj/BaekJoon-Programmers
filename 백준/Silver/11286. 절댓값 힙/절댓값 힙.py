import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, (abs(num), num))
    elif not heap:
        print(0)
    else:
        print(heapq.heappop(heap)[1])