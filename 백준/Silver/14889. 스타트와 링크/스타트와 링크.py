import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
people = list(range(n))
combis = [list(combi) for combi in combinations(people, n//2)]
len_combis = len(combis)
min_v = sys.maxsize

for combi in combis[:len_combis//2]:
    left_combi = [left for left in people if left not in combi]
    start = 0
    link = 0
    for i in combi:
        for j in combi:
            start += graph[i][j]
    
    for i in left_combi:
        for j in left_combi:
            link += graph[i][j]
    
    v = abs(start - link)
    min_v = min(min_v, v)

print(min_v)