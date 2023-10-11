import sys
from collections import defaultdict
input = sys.stdin.readline

def cal(n):
    if n in memo:
        return memo[n]
    memo[n] = cal(n//p) + cal(n//q)
    return memo[n]

n, p, q = map(int, input().split())
memo = defaultdict(int)
memo[0] = 1

print(cal(n))