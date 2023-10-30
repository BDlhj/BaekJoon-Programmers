import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m > 0:
    broken_buttons = list(input().rstrip().split())
else:
    broken_buttons = []
answer = sys.maxsize

for i in range(1000000):
    is_pass = False
    
    if n == 100:
        answer = 0
        break

    for j in str(i):
        if j in broken_buttons:
            is_pass = True
            break
    if is_pass:
        continue

    answer = min(len(str(i)) + abs(n - i), answer)

answer = min(abs(100 - n), answer)
print(answer)