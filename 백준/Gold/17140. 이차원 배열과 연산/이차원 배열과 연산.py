import sys
from collections import Counter
input = sys.stdin.readline

r, c, k = map(int, input().split())
table = [[0] * 100 for _ in range(100)]
for i in range(3):
    table[i][:3] = list(map(int, input().split()))
r_max_len = 3
c_max_len = 3
answer = -1

def r_calc(idx):
    global c_max_len
    
    nums_count_dict = dict(Counter(table[idx]))
    del nums_count_dict[0]
    table[idx] = [0] * 100
    
    nums_count_list = list(nums_count_dict.items())
    nums_count_list.sort(key=lambda x: (x[1], x[0]))
    
    for c in range(len(nums_count_list)):
        if c < 50:
            table[idx][2*c] = nums_count_list[c][0]
            table[idx][2*c+1] = nums_count_list[c][1]

    c_max_len = max(c_max_len, len(nums_count_list) * 2)

def c_calc(idx):
    global r_max_len
    
    c_nums = [table[row][idx] for row in range(100)]
    nums_count_dict = dict(Counter(c_nums))
    del nums_count_dict[0]
    for row in range(100):
        table[row][idx] = 0

    nums_count_list = list(nums_count_dict.items())
    nums_count_list.sort(key=lambda x: (x[1], x[0]))

    for r in range(len(nums_count_list)):
        if r < 50:
            table[2*r][idx] = nums_count_list[r][0]
            table[2*r+1][idx] = nums_count_list[r][1]

    r_max_len = max(r_max_len, len(nums_count_list) * 2)

if table[r-1][c-1] == k:
    print(0)
else:
    for i in range(100):
        if r_max_len >= c_max_len:
            for j in range(r_max_len):
                r_calc(j)
        else:
            for j in range(c_max_len):
                c_calc(j)

        if table[r-1][c-1] == k:
            answer = i + 1
            break

    print(answer)