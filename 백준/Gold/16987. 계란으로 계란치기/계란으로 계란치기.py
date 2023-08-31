import sys
input = sys.stdin.readline

def backtrack(k):
    global cnt, max_v

    if k == n:
        max_v = max(max_v, cnt)
        return

    if broken[k]:
        backtrack(k+1)

    else:
        for i in range(n):
            done = False
            temp = cnt
            if i == k:
                continue
            if not broken[i]:
                done = True
                specs[k][0] -= specs[i][1]
                specs[i][0] -= specs[k][1]
                if specs[k][0] <= 0:
                    broken[k] = True
                    cnt += 1
                if specs[i][0] <= 0:
                    broken[i] = True
                    cnt += 1
            backtrack(k+1)
            if done:
                specs[k][0] += specs[i][1]
                specs[i][0] += specs[k][1]
                broken[k] = False
                broken[i] = False
                cnt = temp
            done = False

n = int(input())
specs = [list(map(int, input().split())) for _ in range(n)]
broken = [False] * n
cnt = 0
max_v = 0

backtrack(0)
print(max_v)