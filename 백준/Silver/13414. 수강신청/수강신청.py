import sys
from collections import defaultdict
input = sys.stdin.readline

k, l = map(int, input().split())
d = defaultdict(int)

for i in range(l):
    d[input().rstrip()] = i+1

d_items = list(d.items())
d_items.sort(key=lambda x: x[1])

if k > len(d_items):
    k = len(d_items)

for i in range(k):
    print(d_items[i][0])