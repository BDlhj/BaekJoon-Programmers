import sys
input = sys.stdin.readline

formula = input().rstrip()
formula_li = []
stack = []
idx = 0
for i in range(len(formula)):
    if formula[i] in ['+', '-']:
        formula_li.append(formula[idx:i])
        formula_li.append(formula[i])
        idx = i+1
formula_li.append(formula[idx:])
is_used = [False] * len(formula_li)

for i in range(len(formula_li)):
    if not is_used[i]:
        if formula_li[i].isdigit():
            stack.append(str(int(formula_li[i])))
            is_used[i] = True
        else:
            if formula_li[i] == '-':
                stack.append(formula_li[i])
                is_used[i] = True
            else:
                stack.append(str(int(stack.pop()) + int(formula_li[i+1])))
                is_used[i], is_used[i+1] = True, True

print(eval(''.join(stack)))