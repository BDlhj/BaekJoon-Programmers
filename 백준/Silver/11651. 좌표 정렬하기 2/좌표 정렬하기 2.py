import sys
input = sys.stdin.readline

n = int(input())
indices = [list(map(int, input().split())) for _ in range(n)]
indices.sort(key=lambda x: (x[1], x[0]))

for index in indices:
    print(' '.join(map(str, index)))