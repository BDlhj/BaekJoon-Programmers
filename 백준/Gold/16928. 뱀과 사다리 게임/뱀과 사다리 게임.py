import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
moves = [0] * 101
counts = [0] * 101

for _ in range(n+m):
    _from, _to = map(int, input().split())
    moves[_from] = _to

q = deque()
q.append(1)
while q:
    cx = q.popleft()
    for i in range(1, 7):
        if cx + i <= 100 and counts[cx + i] == 0:
            counts[cx + i] = counts[cx] + 1
            if moves[cx + i] != 0:
                q.append(moves[cx + i])
                if counts[moves[cx + i]] != 0:
                    counts[moves[cx + i]] = min(counts[moves[cx + i]], counts[cx + i])
                else:
                    counts[moves[cx + i]] = counts[cx + i]
            else:
                q.append(cx + i)

print(counts[100])