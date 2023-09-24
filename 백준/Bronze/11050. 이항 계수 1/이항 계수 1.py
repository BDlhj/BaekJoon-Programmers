import sys
from math import factorial
input = sys.stdin.readline

n, k = map(int, input().split())
answer = int(factorial(n) / (factorial(k) * factorial(n-k)))

print(answer)