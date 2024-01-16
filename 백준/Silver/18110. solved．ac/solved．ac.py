import sys
import math
input = sys.stdin.readline

n = int(input())
difficulties = [int(input()) for _ in range(n)]
difficulties.sort()
mean = 0

n_calculated = n * 0.15
num_to_remove = math.floor(n_calculated) if n_calculated % 1 < 0.5 else math.ceil(n_calculated)
adjusted_difficulties = difficulties[num_to_remove:-num_to_remove] if num_to_remove != 0 else difficulties[:]

if n != 0:
    mean = sum(adjusted_difficulties) / len(adjusted_difficulties)
    mean = math.floor(mean) if mean % 1 < 0.5 else math.ceil(mean)

print(mean)