import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
answer = 0

def recur(T):
    global answer
    if len(T) == len(S):
        if T == S:
            answer = 1
        return
    
    if T[-1] == 'A':
        recur(T[:-1])
    if T[0] == 'B':
        recur(T[1:][::-1])

recur(T)
print(answer)