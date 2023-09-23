import sys
from math import lcm
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())
    _lcm = lcm(M, N)
    answer = -1

    for i in range(_lcm//M):
        if ((M * i + x - y) / N) % 1 == 0.0:
            answer = M * i + x
    print(answer)