import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
relations = [[] for _ in range(n+1)]
visited = [0] * (n+1)
done = False

for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

q = deque()
q.append(a)
while q:
    c = q.popleft()
    for i in relations[c]:
        if not visited[i]:
            q.append(i)
            visited[i] = visited[c] + 1
            if i == b:
                print(visited[i])
                done = True
                break
    if done:
        break

if not done:
    print(-1)