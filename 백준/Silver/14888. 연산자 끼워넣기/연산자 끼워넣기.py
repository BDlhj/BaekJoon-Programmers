import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if x < 0:
        return -(abs(x) // abs(y))
    return x // y

n = int(input())
nums = list(map(int, input().split()))
operator_nums = list(map(int, input().split()))
operator_types = ['+', '-', '*', '/']
all_operators = []
funcs = {'+': plus, '-': minus, '*': mul, '/': div}
expression = [''] * (2*n-1)
max_v = -1e10
min_v = 1e10

# 가능한 연산자 순서 구하기
for i in range(len(operator_nums)):
    all_operators.extend(list(operator_types[i]) * operator_nums[i])
possible_operator_orders = set(permutations(all_operators, n-1))

# 식에 숫자 넣기
for i in range(n):
    expression[2*i] = nums[i]

for possible_operator_order in possible_operator_orders:
    # 식 완성
    for i in range(n-1):
        expression[2*i+1] = possible_operator_order[i]

    stack = deque()
    for s in expression:
        if str(s).isdigit():
            if not stack:
                stack.append(s)
            else:
                stack.append(funcs[stack[1]](stack[0], s))
                stack.popleft()
                stack.popleft()
        
        else:
            stack.append(s)
    
    max_v = max(max_v, stack[0])
    min_v = min(min_v, stack[0])

print(max_v)
print(min_v)