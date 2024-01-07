import sys
from math import comb
input = sys.stdin.readline

n, m = map(int, input().split())
result = comb(n, m)

print(result)
