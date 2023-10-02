import sys
input = sys.stdin.readline

def binary_search(num):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if sg_nums[mid] == num:
            return True
        if sg_nums[mid] > num:
            end = mid - 1
        if sg_nums[mid] < num:
            start = mid + 1

n = int(input())
sg_nums = sorted(list(map(int, input().split())))
m = int(input())
std_nums = list(map(int, input().split()))
answer = []

for std_num in std_nums:
    if binary_search(std_num):
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))

