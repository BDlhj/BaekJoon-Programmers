import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(num):
    while q:
        prst_member = q.popleft()
        for i in d[prst_member]:
            if not visited[i]:
                visited[i] = visited[prst_member] + 1
                q.append(i)

n = int(input())
d = defaultdict(list)
scores = [0] * (n+1)

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    d[a].append(b)
    d[b].append(a)

visited = [0] * (n+1)
for member_num in d:
    q = deque([member_num])
    visited[member_num] = 1
    bfs(member_num)
    score = max(visited) - 1
    scores[member_num] = score
    visited = [0] * (n+1)

min_score = min(scores[1:])
num_of_min_score = scores.count(min_score)
indices = [i for i in range(n+1) if scores[i] == min_score]

print(min_score, num_of_min_score)
print(' '.join(map(str, indices)))