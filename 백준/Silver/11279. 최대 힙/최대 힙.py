import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, (-num, num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)