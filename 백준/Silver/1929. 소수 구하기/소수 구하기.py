import sys
from math import floor
input = sys.stdin.readline

m, n = map(int, input().split())
nums = [num for num in range(m, n+1)]

for num in nums:
    is_prime = True
    if num <= 1:
        continue
    for i in range(2, floor(num**(1/2))+1):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    print(num)