import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(M)])
graph = [[] for _ in range(N+1)]
for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)
deq = deque()
deq.append(R)
visited = [0] * (N+1)
visited[R] = 1
cnt = 2

while deq:
    current_vertex = deq.popleft()
    for vertex in graph[current_vertex]:
        if not visited[vertex]:
            visited[vertex] = cnt
            deq.append(vertex)
            cnt += 1

for i in visited[1:]:
    print(i)