import sys
from itertools import combinations
input = sys.stdin.readline

def calculate(x, y):
    distance = 0
    for c in range(4):
        distance += (x[c] != y[c])
    return distance

t = int(input())

for _ in range(t):
    n = int(input())
    mbtis = input().rstrip().split()
    if n > 32:
        print(0)
    else:
        combis = combinations(mbtis, 3)
        answer = sys.maxsize

        for combi in combis:
            cand = 0
            a, b, c = combi
            cand += calculate(a, b)
            cand += calculate(b, c)
            cand += calculate(c, a)

            answer = min(cand, answer)
        print(answer)

