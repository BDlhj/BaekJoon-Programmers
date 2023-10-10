import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
d = defaultdict(str)

for _ in range(n):
    domain, password = input().rstrip().split()
    d[domain] = password

for _ in range(m):
    print(d[input().rstrip()])
