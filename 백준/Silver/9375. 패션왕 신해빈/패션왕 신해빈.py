import sys
from collections import defaultdict
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    num = int(input())
    d = defaultdict(int)
    answer = 1

    for _ in range(num):
        name, kind = input().rstrip().split()
        d[kind] += 1
    
    for v in d.values():
        answer *= (v+1)

    print(answer-1)
