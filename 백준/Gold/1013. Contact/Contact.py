import sys
import re
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    wave = input().rstrip()
    pattern = re.compile(r'(100+1+|01)+')
    answer = re.fullmatch(pattern, wave)
    
    if answer:
        print('YES')
    else:
        print('NO')