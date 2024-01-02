import sys
input = sys.stdin.readline

n = int(input())
volumes = sorted(list(map(int, input().split())), reverse=True)
answer = volumes[0]

for i in range(1, len(volumes)):
    answer += volumes[i] / 2

print(answer)