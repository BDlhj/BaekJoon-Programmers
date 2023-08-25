import sys
input = sys.stdin.readline

n, m = map(int, input().split())
is_used = [False] * (n+1)
answer = [''] * m

def backtrack(k):
    if k == m:
        print(' '.join(answer))
        return
    
    for i in range(1, n+1):
        answer[k] = str(i)
        backtrack(k+1)

backtrack(0)