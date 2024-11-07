def solution(topping):
    answer = 0
    
    forward = [0] * (len(topping))
    forward_set = set()
    backward = [0] * (len(topping))
    backward_set = set()
    
    for i in range(len(topping)):
        if topping[i] not in forward_set:
            forward_set.add(topping[i])
        forward[i] = len(forward_set)
    
    for i in range(len(topping) - 1, -1, -1):
        if topping[i] not in backward_set:
            backward_set.add(topping[i])
        backward[i] = len(backward_set)
    
    for i in range(len(forward) - 1):
        if forward[i] == backward[i + 1]:
            answer += 1
    
    return answer