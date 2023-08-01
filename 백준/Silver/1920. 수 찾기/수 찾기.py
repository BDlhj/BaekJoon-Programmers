n = int(input())
num_array = set(input().split())
m = int(input())
check_nums = input().split()

for i in check_nums:
    if i in num_array:
        print('1')
    else:
        print('0')