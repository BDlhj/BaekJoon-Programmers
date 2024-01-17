import sys
from collections import deque
input = sys.stdin.readline

# 유저 수, 친구 관계 수
N, M = map(int, input().split())
relations = [[] for _ in range(N+1)]
cand = []

for _ in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

for num in range(1, N+1):
    dist = [0] * (N+1)
    q = deque([num])
    bacon_num = 0

    while q:
        cur = q.popleft()
        for i in relations[cur]:
            if not dist[i]:
                dist[i] = dist[cur] + 1
                q.append((i))
    
    dist[num] = 0
    cand.append((sum(dist), num))

cand.sort()

print(cand[0][1])