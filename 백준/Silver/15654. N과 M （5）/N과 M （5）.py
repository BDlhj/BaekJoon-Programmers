import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

is_used = [False] * n
answer = [''] * m

def backtrack(k):
    if k == m:
        print(' '.join(answer))
        return

    for i in range(n):
        if not is_used[i]:
            answer[k] = str(nums[i])
            is_used[i] = True
            backtrack(k+1)
            is_used[i] = False

backtrack(0)