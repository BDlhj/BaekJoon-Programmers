import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a_reversed = list(reversed(a))
stack = []
answer = []

for i in a_reversed:
    while stack and i >= stack[-1]:
        stack.pop()
    if not stack:
        stack.append(i)
        answer.append(-1)
    if i < stack[-1]:
        answer.append(stack[-1])
    stack.append(i)

answer.reverse()

print(' '.join(map(str, answer)))