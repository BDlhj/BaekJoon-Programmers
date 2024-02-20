import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
from_where = [-1] * 100001
from_where[N] = 0
deq = deque()
deq.append(N)
path = []

while deq:
    current_loc = deq.popleft()
    if current_loc == K:
        break
    if 0 <= current_loc - 1 <= 100000 and from_where[current_loc-1] == -1:
        from_where[current_loc-1] = current_loc
        deq.append(current_loc-1)
    if 0 <= current_loc + 1 <= 100000 and from_where[current_loc+1] == -1:
        from_where[current_loc+1] = current_loc
        deq.append(current_loc+1)
    if 0 <= current_loc * 2 <= 100000 and from_where[current_loc*2] == -1:
        from_where[current_loc*2] = current_loc
        deq.append(current_loc*2)

current = K
while True:
    if current == N:
        break
    path.append(from_where[current])
    current = from_where[current]

print(len(path))
print(*path[::-1], K)
