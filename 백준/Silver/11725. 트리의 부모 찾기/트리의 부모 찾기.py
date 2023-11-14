import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)

    while q:
        prst = q.popleft()
        for next in graph[prst]:
            if answer[next] == 0:
                answer[next] = prst
                q.append(next)

n = int(input())
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()
print('\n'.join(map(str, answer[2:])))