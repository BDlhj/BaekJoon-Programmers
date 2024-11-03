from math import ceil


def solution(progresses, speeds):
    answer = []
    stack = []
    
    remain_progresses = [100 - progress for progress in progresses]
    days = [ceil(remain_progress / speed) for remain_progress, speed in zip(remain_progresses, speeds)]
    print(days)
    
    for day in days:
        if not stack:
            stack.append(day)
        else:
            if day > stack[0]:
                answer.append(len(stack))
                stack.clear()
            stack.append(day)
    answer.append(len(stack))
    
    return answer