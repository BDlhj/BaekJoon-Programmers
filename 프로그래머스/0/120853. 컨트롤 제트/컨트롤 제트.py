def solution(s):
    stack = []
    input_s = s.split()
    for element in input_s:
        if element == 'Z':
            stack.pop()
        else:
            stack.append(int(element))
    
    return sum(stack)
    