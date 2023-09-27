import sys
from math import ceil
input = sys.stdin.readline

n, k, l = map(int, input().split())
answer = 1

while ceil(k/2) != ceil(l/2):
    k = ceil(k/2)
    l = ceil(l/2)
    answer += 1

print(answer)