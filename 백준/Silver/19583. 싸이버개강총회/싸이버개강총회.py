import sys
from collections import defaultdict
input = sys.stdin.readline

s, e, q = input().rstrip().split()
log = defaultdict(list)
answer = 0

while True:
    try:
        time, name = input().rstrip().split()
        if time <= q:
            log[name].append(time)
    except:
        break

for name in log:
    if len(log[name]) >= 2 and (log[name][0] <= s and e <= log[name][-1] <= q):
        answer += 1

print(answer)