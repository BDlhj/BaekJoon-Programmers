import sys
import math
input = sys.stdin.readline

_min, _max = map(int, input().split())
divided = [False] * (_max - _min + 1)

for num in range(2, math.floor(math.sqrt(_max)) + 1):
    num_squared = num ** 2
    for target_num in range( (((_min-1)//num_squared)+1)*num_squared , _max+1, num_squared):
        if target_num % (num_squared) == 0:
            divided[target_num - _min] = True

print(len(divided) - sum(divided))
