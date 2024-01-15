import sys
input = sys.stdin.readline

while True:
    tc = input().rstrip()
    if tc == '0':
        break
    
    if tc == tc[::-1]:
        print('yes')
    else:
        print('no')
