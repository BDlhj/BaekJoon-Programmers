import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    root_of_x = find(parents[x])
    parents[x] = root_of_x
    return root_of_x

def union(x, y):
    root_of_x = find(x)
    root_of_y = find(y)

    if root_of_x < root_of_y:
        parents[root_of_y] = root_of_x
    elif root_of_x > root_of_y:
        parents[root_of_x] = root_of_y

# 집합 개수, 연산 개수
n, m = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(m)]
parents = list(range(n+1))

for operation in operations:
    operator, operand_1, operand_2 = operation
    if operator == 0:
        union(operand_1, operand_2)
    elif find(operand_1) == find(operand_2):
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
