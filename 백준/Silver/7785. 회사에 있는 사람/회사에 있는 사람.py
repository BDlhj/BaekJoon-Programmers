import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
d = defaultdict(int)

for _ in range(n):
    name, action = input().rstrip().split()
    if action == 'enter':
        d[name] += 1
    else:
        d[name] -= 1

answer = [name for name in d if d[name] > 0]
print('\n'.join(sorted(answer, reverse=True)))