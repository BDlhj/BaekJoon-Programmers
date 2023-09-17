import sys
input = sys.stdin.readline

n = int(input())
infos = [list(input().split()) for _ in range(n)]

infos.sort(key=lambda x: (100-int(x[1]), int(x[2]), 100-int(x[3]), x[0]))
for info in infos:
    print(info[0])