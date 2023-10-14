import sys
from collections import deque, defaultdict
input = sys.stdin.readline

num_of_com = int(input())
pairs = int(input())
d = defaultdict(list)
q = deque()
visited = defaultdict(int)
answer = 0

for _ in range(pairs):
    s, e = map(int, input().split())
    d[s].append(e)
    d[e].append(s)

q.append(1)
visited[1] = True

while q:
    prst_v = q.popleft()
    for i in d[prst_v]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            answer += 1

print(answer)