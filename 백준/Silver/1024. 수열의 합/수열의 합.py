import sys
input = sys.stdin.readline

n, l = map(int, input().split())
answer = -1
num = 0

for i in range(l, 101):
    if (n/i - i/2 + 1/2) % 1 == 0:
        answer = int(n/i - i/2 + 1/2)
        if answer >= 0:
            num = i
            break
        else:
            answer = -1

if answer != -1:
    for j in range(num):
        print(answer + j, end=' ')
else:
    print(answer)
