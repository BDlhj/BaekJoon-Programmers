import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, list(input().rstrip())))
stack = []

for i in num:
    if len(stack) == 0 or k == 0:
        stack.append(i)
    else:
        while len(stack) and stack[-1] < i:
            stack.pop()
            k -= 1
            if k == 0:
                break
        stack.append(i)

for _ in range(k):
    stack.pop()

print(''.join(map(str, stack)))
