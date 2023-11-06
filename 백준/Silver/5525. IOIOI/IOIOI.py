import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
answer = 0

p = []
for i in range(2*n+1):
    if i % 2 == 0:
        p.append('I')
    else:
        p.append('O')

p_str = ''.join(p)
p_len = 2 * n + 1

for i in range(m-p_len+1):
    if s[i:i+p_len] == p_str:
        answer += 1

print(answer)