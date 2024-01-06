import sys
from math import gcd
input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
fraction_sum = [a1 * b2 + a2 * b1, b1 * b2]

divider = gcd(fraction_sum[0], fraction_sum[1])
fraction_sum = [fraction_sum[0] // divider, fraction_sum[1] // divider]

print(' '.join(map(str, fraction_sum)))