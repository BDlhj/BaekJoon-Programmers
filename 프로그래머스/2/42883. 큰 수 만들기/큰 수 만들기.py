def solution(number, k):
    stack = []
    count = 0

    for num in number:
        while stack and stack[-1] < num and count < k:
            stack.pop()
            count += 1
        stack.append(num)
    left_count = k - count

    return ''.join(stack)[:len(stack) - left_count]