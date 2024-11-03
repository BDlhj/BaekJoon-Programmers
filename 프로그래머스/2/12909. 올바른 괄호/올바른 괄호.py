def solution(string):
    stack = []
    
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
    
    if stack:
        return False
    return True