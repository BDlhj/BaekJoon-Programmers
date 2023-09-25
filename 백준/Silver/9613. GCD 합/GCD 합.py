import sys
from math import gcd
from itertools import combinations
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    combis = combinations(nums[1:], 2)
    gcd_sum = 0

    for combi in combis:
        gcd_sum += gcd(combi[0], combi[1])

    print(gcd_sum)