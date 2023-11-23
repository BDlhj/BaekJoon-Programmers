import sys
input = sys.stdin.readline

s = input().rstrip()
explosion_s = input().rstrip()

stack = []
len_of_explosion_s = len(explosion_s)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-len_of_explosion_s:]) == explosion_s:
        for _ in range(len_of_explosion_s):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')