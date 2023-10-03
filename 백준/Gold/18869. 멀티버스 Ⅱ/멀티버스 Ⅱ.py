import sys
from itertools import combinations
input = sys.stdin.readline

def compress(li):
    new_li = sorted(list(set(li)))
    d = {v: i for i, v in enumerate(new_li)}
    indices = [d[v] for v in li]
    return indices

m, n = map(int, input().split())
galaxy = [compress(list(map(int, input().split()))) for _ in range(m)]
answer = 0

for combi in combinations(range(m), 2):
    answer += (galaxy[combi[0]] == galaxy[combi[1]])

print(answer)