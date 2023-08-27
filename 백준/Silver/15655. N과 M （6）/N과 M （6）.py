import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

answer = ['0'] + ([''] * m)
is_used = [False] * n

def backtrack(k):
    if k == m+1:
        print(' '.join(answer[1:]))
        return

    for i in range(n):
        if not is_used[i] and nums[i] > int(answer[k-1]):
            answer[k] = str(nums[i])
            is_used[i] = True
            backtrack(k+1)
            is_used[i] = False

backtrack(1)