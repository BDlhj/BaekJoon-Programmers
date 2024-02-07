import sys
input = sys.stdin.readline

string = input().rstrip()
N = len(string)
answer = -1

if string != string[::-1]:
    answer = N
elif N > 1 and string != string[0] * N:
    answer = N - 1
print(answer)
