import sys
input = sys.stdin.readline

case = int(input())
commands = ['<', '>', '-']

for _ in range(case):
    s = input().strip()
    cursor_left = []
    cursor_right = []
    
    for i in s:
        if i not in commands:
            cursor_left.append(i)
        if i == '<':
            if cursor_left:
                cursor_right.append(cursor_left.pop())
        if i == '>':
            if cursor_right:
                cursor_left.append(cursor_right.pop())
        if i == '-':
            if cursor_left:
                cursor_left.pop()
    answer = cursor_left + list(reversed(cursor_right))
    print(''.join(answer))