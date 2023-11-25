import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

distances = [sys.maxsize] * (n+1)
distances[start] = 0
queue = []
heapq.heappush(queue, (distances[start], start))

while queue:
    dist, vertex = heapq.heappop(queue)

    if distances[vertex] < dist:
        continue
    
    for n_vertex, n_dist in graph[vertex]:
        distance = dist + n_dist
        if distance < distances[n_vertex]:
            distances[n_vertex] = distance
            heapq.heappush(queue, (distance, n_vertex))

print(distances[end])