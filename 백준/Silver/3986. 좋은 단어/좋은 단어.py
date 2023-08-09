import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range(n):
    word = input().strip()
    stack = []
    for c in word:
        if not stack:
            stack.append(c)
            continue
        if c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        answer += 1
    
print(answer)