from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total_sum = sum(queue1) + sum(queue2)
    target_sum = total_sum / 2
    if target_sum % 1 == 0:
        target_sum = int(target_sum)
    else:
        return -1
    
    sub_1 = sum(queue1) - target_sum
    sub_2 = sum(queue2) - target_sum
    cnt = 0
    if sub_1 == sub_2:
        return cnt
    for i in range(300009):
        if sub_1 > sub_2:
            sub_1 -= queue1[0]
            sub_2 += queue1[0]
            queue2.append(queue1.popleft())
            
        else:
            sub_1 += queue2[0]
            sub_2 -= queue2[0]
            queue1.append(queue2.popleft())
        cnt += 1
        if sub_1 == sub_2:
            return cnt
    return -1