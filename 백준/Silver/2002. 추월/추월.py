import sys
input = sys.stdin.readline

n = int(input())
in_cars = {}
out_cars = []
answer = 0

for idx in range(1, n+1):
    in_cars[input().rstrip()] = idx

for _ in range(n):
    out_cars.append(input().rstrip())

for i in range(n):
    for j in range(i+1, n):
        if in_cars[out_cars[i]] > in_cars[out_cars[j]]:
            answer += 1
            break

print(answer)