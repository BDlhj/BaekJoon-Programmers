def solution(array, commands):
    answer = []
    for command in commands:
        start, end, target = command
        answer.append(sorted(array[start - 1:end])[target - 1])
    
    return answer