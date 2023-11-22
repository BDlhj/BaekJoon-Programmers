import sys
from math import floor, lcm
input = sys.stdin.readline

_gcd, _lcm = map(int, input().split())
std = _lcm / _gcd
d = []

for i in range(1, floor(std**(1/2))+1):
    if std % i == 0:
        d.append((_gcd * i, _gcd * int(std // i)))

answer = [i for i in d if lcm(i[0], i[1]) == _lcm]
print(' '.join(map(str, answer[-1])))