import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
st = en = 0
partial_sum = nums[en]
min_len = sys.maxsize

while st < n:
    if partial_sum >= s:
        min_len = min(min_len, en-st+1)
        if min_len == 1:
            break
        partial_sum -= nums[st]
        st += 1
    else:
        en += 1
        if en == n:
            break
        partial_sum += nums[en]

if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)