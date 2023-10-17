import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
s = sorted([input().rstrip() for _ in range(n)])
cand = [input().rstrip() for _ in range(m)]
answer = 0

for word in cand:
    idx = bisect.bisect_left(s, word)
    if idx == n:
        continue
    if word == s[idx]:
        answer += 1

print(answer)