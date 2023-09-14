import sys
input = sys.stdin.readline

def check(line):
    for prst in range(1, n):
        if abs(line[prst] - line[prst-1]) > 1:
            return False
        if line[prst] > line[prst-1]:
            for i in range(l):
                if prst-i-1 < 0 or slope[prst-i-1] or line[prst-1] != line[prst-i-1]:
                    return False
                if line[prst-1] == line[prst-i-1]:
                    slope[prst-i-1] = True
        elif line[prst] < line[prst-1]:
            for i in range(l):
                if prst+i >= n or slope[prst+i] or line[prst] != line[prst+i]:
                    return False
                if line[prst] == line[prst+i]:
                    slope[prst+i] = True
    return True

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for row in range(n):
    slope = [False] * n
    if check([board[row][col] for col in range(n)]):
        answer += 1

for col in range(n):
    slope = [False] * n
    if check([board[row][col] for row in range(n)]):
        answer += 1

print(answer)