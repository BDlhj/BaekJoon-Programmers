import sys
import heapq
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])
weights = [float('inf')] * (V+1)
deq = []

heapq.heappush(deq, [0, K])
weights[K] = 0

while deq:
    current_weight, current_vertex = heapq.heappop(deq)
    if weights[current_vertex] < current_weight:
        continue
    for next_weight, next_vertex in graph[current_vertex]:
        n_weight = current_weight + next_weight
        if n_weight < weights[next_vertex]:
            weights[next_vertex] = n_weight
            heapq.heappush(deq, [n_weight, next_vertex])

for i in range(1, V+1):
    if weights[i] == float('inf'):
        sys.stdout.write('INF\n')
    else:
        sys.stdout.write(f'{weights[i]}\n')