import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0
while (b > a) and (b % 2 == 0 or str(b)[-1] == '1'):
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
        cnt += 1
    else:
        b //= 2
        cnt += 1

if a == b:
    print(cnt+1)
else:
    print(-1)