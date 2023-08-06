import sys
input = sys.stdin.readline

n = int(input())
stack = []
operators = []
flag = True
num = 0

for _ in range(n):
    target = int(input())

    if target > num:
        stack += list(range(num+1, target+1))
        operators += ['+'] * (target-num)
        num = target
    
    if target == stack[-1]:
        stack.pop()
        operators.append('-')
    else:
        flag = False
        break

if flag:
    for i in operators:
        print(i)
else:
    print('NO')