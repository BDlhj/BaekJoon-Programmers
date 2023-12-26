import sys
import math
input = sys.stdin.readline

num = 10000
is_prime = [True for i in range(num+1)]

for i in range(2, int(math.sqrt(num))+1):
    if is_prime[i]:
        j = 2
        while i * j <= num:
            is_prime[i * j] = False
            j += 1

prime_nums = [i for i in range(2, num+1) if is_prime[i]]

t = int(input())
for _ in range(t):
    n = int(input())
    min_gap = sys.maxsize
    first = second = 0

    for prime_num in prime_nums:
        if prime_num < n and n - prime_num in prime_nums:
            gap = abs(n - prime_num*2)
            if gap < min_gap:
                min_gap = gap
                first = prime_num
                second = n - prime_num
    
    print(first, second)