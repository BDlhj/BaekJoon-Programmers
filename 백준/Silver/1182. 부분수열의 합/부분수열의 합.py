import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
sum_result = 0

def backtrack(k):
    global sum_result, cnt
    if k == n:
        return
    
    sum_result += nums[k]
    if sum_result == s:
        cnt += 1
    backtrack(k+1)
    sum_result -= nums[k]

    backtrack(k+1)

backtrack(0)

print(cnt)