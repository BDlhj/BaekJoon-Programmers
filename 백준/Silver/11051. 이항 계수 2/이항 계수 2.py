import sys
from math import factorial
input = sys.stdin.readline

n, k = map(int, input().split())
answer = factorial(n) // (factorial(k) * factorial(n-k))

print(answer % 10007)