import sys
input = sys.stdin.readline

arr = input()
l_paren = '('
r_paren = ')'
stack = []
prev = None
answer = 0

for i in arr:
    if i == l_paren:
        stack.append(i)
        prev = i
    if i == r_paren:
        stack.pop()
        if prev == l_paren:
            answer += len(stack)
        else:
            answer += 1
        prev = i
print(answer)