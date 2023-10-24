import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
spots = sorted(list(map(int, input().split())))

distances = []
for i in range(1, n):
    distances.append(spots[i] - spots[i-1])
distances.sort()

if k > n:
    print('0')
else:
    for _ in range(k-1):
        distances.pop()

    print(sum(distances))