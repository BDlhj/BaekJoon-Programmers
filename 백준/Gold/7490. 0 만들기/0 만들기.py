import sys
from itertools import product
input = sys.stdin.readline

tc = int(input())
for time in range(tc):
    N = int(input())
    expression = [''] * (2*N-1)
    operators = ['+', '-', ' ']
    operator_products = list(product(operators, repeat=N-1))
    expressions = list()

    for i in range(1, N+1):
        expression[2*(i-1)] = i

    for operator_product in operator_products:
        for j in range(len(operator_product)):
            expression[2*j+1] = operator_product[j]
            
        final_expression = eval(''.join(map(str, expression)).replace(' ', ''))
    
        if final_expression == 0 and expression not in expressions:
            expressions.append(''.join(map(str, expression)))
    
    expressions.sort()
    for expression in expressions:
        print(expression)

    if time == tc-1:
        break
    print()