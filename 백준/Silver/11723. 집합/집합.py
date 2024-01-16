import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().rstrip().split()
    if command[0] == 'add':
        S |= {int(command[1])}
    elif command[0] == 'remove':
        S -= {int(command[1])}
    elif command[0] == 'check':
        print(int(int(command[1]) in S))
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S -= {int(command[1])}
        else:
            S |= {int(command[1])}
    elif command[0] == 'all':
        S = set(range(1, 21))
    else:
        S = set()
