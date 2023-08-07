import sys
input = sys.stdin.readline

s = input()
m = int(input())

cursor_left = list(s.strip())
cursor_right = []

def function(cursor_left, cursor_right, command):
    if command[0] == 'L':
        if cursor_left:
            cursor_right.append(cursor_left.pop())
    elif command[0] == 'D':
        if cursor_right:
            cursor_left.append(cursor_right.pop())
    elif command[0] == 'B':
        if cursor_left:
            cursor_left.pop()
    elif command[0] == 'P':
        cursor_left.append(command[1])

for _ in range(m):
    command = input().split()
    function(cursor_left, cursor_right, command)

answer = cursor_left + list(reversed(cursor_right))
print(''.join(answer))