import sys
input = sys.stdin.readline

def backtrack(x, k):
    if x == pick_num+1:
        print(' '.join(answer[1:]))
        return

    for i in range(k):
        if not is_used[i] and s[i] > int(answer[x-1]):
            answer[x] = str(s[i])
            is_used[i] = True
            backtrack(x+1, k)
            is_used[i] = False

pick_num = 6
while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    k = nums[0]
    s = nums[1:]
    answer = ['0'] + ([''] * pick_num)
    is_used = [False] * k
    
    backtrack(1, k)
    print()