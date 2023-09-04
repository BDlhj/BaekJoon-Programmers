import sys
from collections import deque
input = sys.stdin.readline

# 1번 톱니바퀴 회전
def rotate_1(direction):
    if is_checked[0]:
        return

    is_checked[0] = True

    # 시계방향으로 돌리기
    if direction == 1:
        # 2번 톱니바퀴 회전 여부 확인
        if wheels[0][right_checkpoint] != wheels[1][left_checkpoint]:
            rotate_2(-direction)
        wheels[0].appendleft(wheels[0].pop())
    
    # 반시계방향으로 돌리기
    if direction == -1:
        # 2번 톱니바퀴 회전 여부 확인
        if wheels[0][right_checkpoint] != wheels[1][left_checkpoint]:
            rotate_2(-direction)
        wheels[0].append(wheels[0].popleft())

# 2번 톱니바퀴 회전
def rotate_2(direction):
    if is_checked[1]:
        return

    is_checked[1] = True
    
    # 시계방향으로 돌리기
    if direction == 1:
        # 1번 톱니바퀴 회전 여부 확인
        if wheels[1][left_checkpoint] != wheels[0][right_checkpoint]:
            rotate_1(-direction)

        # 3번 톱니바퀴 회전 여부 확인
        if wheels[1][right_checkpoint] != wheels[2][left_checkpoint]:
            rotate_3(-direction)
        wheels[1].appendleft(wheels[1].pop())
    
    # 반시계방향으로 돌리기
    if direction == -1:
        # 1번 톱니바퀴 회전 여부 확인
        if wheels[1][left_checkpoint] != wheels[0][right_checkpoint]:
            rotate_1(-direction)

        # 3번 톱니바퀴 회전 여부 확인
        if wheels[1][right_checkpoint] != wheels[2][left_checkpoint]:
            rotate_3(-direction)
        wheels[1].append(wheels[1].popleft())

# 3번 톱니바퀴 회전
def rotate_3(direction):
    if is_checked[2]:
        return

    is_checked[2] = True
    
    # 시계방향으로 돌리기
    if direction == 1:
        # 2번 톱니바퀴 회전 여부 확인
        if wheels[2][left_checkpoint] != wheels[1][right_checkpoint]:
            rotate_2(-direction)

        # 4번 톱니바퀴 회전 여부 확인
        if wheels[2][right_checkpoint] != wheels[3][left_checkpoint]:
            rotate_4(-direction)
        wheels[2].appendleft(wheels[2].pop())
    
    # 반시계방향으로 돌리기
    if direction == -1:
        # 2번 톱니바퀴 회전 여부 확인
        if wheels[2][left_checkpoint] != wheels[1][right_checkpoint]:
            rotate_2(-direction)

        # 4번 톱니바퀴 회전 여부 확인
        if wheels[2][right_checkpoint] != wheels[3][left_checkpoint]:
            rotate_4(-direction)
        wheels[2].append(wheels[2].popleft())

# 4번 톱니바퀴 회전
def rotate_4(direction):
    if is_checked[3]:
        return

    is_checked[3] = True
    
    # 시계방향으로 돌리기
    if direction == 1:
        # 3번 톱니바퀴 회전 여부 확인
        if wheels[3][left_checkpoint] != wheels[2][right_checkpoint]:
            rotate_3(-direction)
        wheels[3].appendleft(wheels[3].pop())
    
    # 반시계방향으로 돌리기
    if direction == -1:
        # 3번 톱니바퀴 회전 여부 확인
        if wheels[3][left_checkpoint] != wheels[2][right_checkpoint]:
            rotate_3(-direction)
        wheels[3].append(wheels[3].popleft())

# N극은 0, S극은 1
wheels = [deque(map(int, list(input().rstrip()))) for _ in range(4)]

# 회전 횟수
k = int(input())

# 1은 시계방향, -1은 반시계방향
instructions = [list(map(int, input().split())) for _ in range(k)]

right_checkpoint = 2
left_checkpoint = 6
score_checkpoint = 0
score = 0

rotate_funcs = {1: rotate_1, 2: rotate_2, 3: rotate_3, 4: rotate_4}

for instruction in instructions:
    is_checked = [False] * 4
    wheel_num = instruction[0]
    direction = instruction[1]
    rotate_funcs[wheel_num](direction)

for num in range(len(wheels)):
    if wheels[num][score_checkpoint]:
        score += 2 ** num

print(score)