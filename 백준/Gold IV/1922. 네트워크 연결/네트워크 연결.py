import sys
import heapq
input = sys.stdin.readline

# 프림 알고리즘 활용
N = int(input())
M = int(input())

network = [[] for _ in range(N+1)]
net_cost_infos = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[2])
visited = [False] * (N+1)
edges = [(0, 1)]
heapq.heapify(edges)
min_cost = 0

# 연결 정보 초기화
for info in net_cost_infos:
    a, b, c = info
    network[a].append((c, b))
    network[b].append((c, a))

while edges:
    cost, current_vertex = heapq.heappop(edges)
    if not visited[current_vertex]:
        min_cost += cost
        visited[current_vertex] = True
        for i in network[current_vertex]:
            if not visited[i[1]]:
                heapq.heappush(edges, i)

print(min_cost)