import sys
input = sys.stdin.readline
            
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    v = []

    for i in a:
        v.append((i, 0))
        

    for j in b:
        v.append((j, 1))

    v.sort()

    cnt = 0
    ans = 0

    for i in range(n + m):
        if v[i][1] == 0:
            ans += cnt
        else:
            cnt += 1

    print(ans)