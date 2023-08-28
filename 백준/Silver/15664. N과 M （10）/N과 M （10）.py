import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
is_used = [False] * n
answer = ['0'] + ([''] * m)
answer_list = ['']

def backtrack(k):
    if k == m+1:
        answer_list.append(answer[:])
        return

    for i in range(n):
        if not is_used[i] and nums[i] >= int(answer[k-1]):
            answer[k] = str(nums[i]) 
            if answer not in answer_list:
                is_used[i] = True
                backtrack(k+1)
                is_used[i] = False

backtrack(1)

for i in answer_list[1:]:
    print(' '.join(i[1:]))