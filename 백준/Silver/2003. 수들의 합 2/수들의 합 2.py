import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

st, en = 0, 0
partial_sum = nums[en]

while en <= n-1:
    if partial_sum == m:
        answer += 1
        en += 1
        if en == n:
            break
        partial_sum += nums[en]
    elif partial_sum < m:
        en += 1
        if en == n:
            break
        partial_sum += nums[en]
    else:
        partial_sum -= nums[st]
        st += 1

print(answer)