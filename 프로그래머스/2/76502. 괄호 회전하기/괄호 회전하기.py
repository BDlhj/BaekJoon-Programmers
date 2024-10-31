from collections import deque


def is_correct(string):
    stack = []
    for s in string:
        if s in ['(', '[', '{']:
            stack.append(s)
        else:
            if not stack:
                return False
            elif s == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif s == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif s == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()

    if stack:
        return False
    return True


def solution(s):
    ans = 0
    s = deque(s)
    for _ in range(len(s)):
        if is_correct(s):
            ans += 1
        s.append(s.popleft())
    return ans