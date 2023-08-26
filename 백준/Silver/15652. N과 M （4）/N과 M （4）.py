import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = ['0'] + ([''] * m)

def backtrack(k):
    if k == m+1:
        print(' '.join(answer[1:]))
        return
    
    for i in range(1, n+1):
        if i >= int(answer[k-1]):
            answer[k] = str(i)
            backtrack(k+1)
    
backtrack(1)