import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
descendings = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        descendings.append(int(''.join(reversed(list(map(str, j))))))
descendings.sort()

if n >= len(descendings):
    print(-1)

else:
    print(descendings[n])