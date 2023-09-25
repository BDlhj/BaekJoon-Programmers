import sys
from math import factorial
input = sys.stdin.readline

fact = factorial(int(input()))
fact_reversed = str(fact)[::-1]
cnt = 0

for i in range(len(fact_reversed)-1):
    if fact_reversed[i] == '0':
        cnt += 1
    else:
        break

print(cnt)