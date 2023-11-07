import sys
input = sys.stdin.readline

n = list(input().rstrip())

if '0' not in n:
    print(-1)
else:
    if sum(map(int, n)) % 3 == 0:
        n.sort(reverse=True)
        print(''.join(n))
    else:
        print(-1)