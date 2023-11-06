import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
cur = 0
p_1_cnt = 0
answer = 0

while cur < m - 1:
    if s[cur:cur+3] == 'IOI':
        p_1_cnt += 1
        cur += 2
        if p_1_cnt == n:
            answer += 1
            p_1_cnt -= 1
    else:
        p_1_cnt = 0
        cur += 1

print(answer)
