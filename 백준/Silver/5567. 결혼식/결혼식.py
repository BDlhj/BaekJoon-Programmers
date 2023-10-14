import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
d = defaultdict(list)
q = deque()
visited = [0] * (n+1)
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
    
q.append(1)
visited[1] = 1

while q:
    prst_v = q.popleft()
    for i in d[prst_v]:
        if visited[i] == 0:
            visited[i] = visited[prst_v] + 1
            if visited[i] > 3:
                continue
            q.append(i)
            answer += 1

print(answer)