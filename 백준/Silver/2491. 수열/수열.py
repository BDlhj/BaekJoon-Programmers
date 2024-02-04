import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = 1

st_idx = 0
asc_cnt = 1
for i in range(1, n):
    if nums[st_idx] <= nums[i]:
        asc_cnt += 1
        answer = max(answer, asc_cnt)
    else:
        asc_cnt = 1
    st_idx = i

st_idx = 0
desc_cnt = 1
for i in range(1, n):
    if nums[st_idx] >= nums[i]:
        desc_cnt += 1
        answer = max(answer, desc_cnt)
    else:
        desc_cnt = 1
    st_idx = i

print(answer)
