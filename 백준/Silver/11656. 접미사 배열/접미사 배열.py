import sys
input = sys.stdin.readline

s = input().rstrip()
answer = [s[i:] for i in range(len(s))]
print(*sorted(answer), sep='\n')