import sys
input = sys.stdin.readline

n = int(input())
volumes = [int(input()) for _ in range(n)] + ([0] * 10000)
accumulated_max_volume = [0] * (n+3)

accumulated_max_volume[0] = volumes[0]
accumulated_max_volume[1] = volumes[0] + volumes[1]
accumulated_max_volume[2] = max(accumulated_max_volume[1], accumulated_max_volume[0] + volumes[2], volumes[1] + volumes[2])

for i in range(3, n):
    accumulated_max_volume[i] = max(accumulated_max_volume[i-1], volumes[i] + volumes[i-1] + accumulated_max_volume[i-3], volumes[i] + accumulated_max_volume[i-2])

print(accumulated_max_volume[n-1])