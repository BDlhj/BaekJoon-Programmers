import sys
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
values.sort()
closest = sys.maxsize

for i in range(n-2):
    s = i+1
    e = n-1
    target = -values[i]
    while s < e:
        if abs((values[s] + values[e]) - target) < closest:
            closest = abs((values[s] + values[e]) - target)
            answer = [values[i], values[s], values[e]]
        if values[s] + values[e] > target:
            e -= 1
        elif values[s] + values[e] < target:
            s += 1
        elif values[s] + values[e] == target:
            break

print(' '.join(map(str,answer)))