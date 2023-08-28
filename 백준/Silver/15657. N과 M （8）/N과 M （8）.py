import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = ['0'] + ([''] * m)

def backtrack(k):
    if k == m+1:
        print(' '.join(answer[1:]))
        return
    
    for i in range(n):
        if nums[i] >= int(answer[k-1]):
            answer[k] = str(nums[i])
            backtrack(k+1)
    
backtrack(1)