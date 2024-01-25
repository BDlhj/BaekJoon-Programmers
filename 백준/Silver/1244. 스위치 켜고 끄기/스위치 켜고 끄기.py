import sys
input = sys.stdin.readline

num_of_switch = int(input())
states_of_switch = list(map(int, input().split()))
num_of_student = int(input())
students_info = [list(map(int, input().split())) for _ in range(num_of_student)]

for idx in range(num_of_student):
    sex, given_num  = students_info[idx]
    if sex == 1:
        for change_idx in range(given_num-1, num_of_switch, given_num):
            states_of_switch[change_idx] = abs(states_of_switch[change_idx]-1)
    else:
        left_idx = (given_num-1) - 1
        right_idx = (given_num-1) + 1
        while (left_idx >= 0 and right_idx < num_of_switch) and (states_of_switch[left_idx] == states_of_switch[right_idx]):
            left_idx -= 1
            right_idx += 1
        for change_idx in range(left_idx+1, right_idx):
            states_of_switch[change_idx] = abs(states_of_switch[change_idx]-1)

cnt = 0
for i in range(num_of_switch):
    print(states_of_switch[i], end=' ')
    cnt += 1
    if cnt % 20 == 0:
        print()