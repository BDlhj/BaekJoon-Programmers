import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()
answer = [''] * m

def backtrack(k):
    if k == m:
        print(' '.join(answer))
        return

    for i in range(len(nums)):
        answer[k] = str(nums[i])
        backtrack(k+1)

backtrack(0)