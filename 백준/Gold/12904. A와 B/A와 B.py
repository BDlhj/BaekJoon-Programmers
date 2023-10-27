import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while t and s != t:
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]

if t:
    print(1)
else:
    print(0)