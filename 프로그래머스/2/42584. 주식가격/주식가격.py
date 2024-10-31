def solution(prices):
    ans = {}
    stack = []
    
    for time, price in enumerate(prices):
        if not stack:
            stack.append((time, price))
        else:
            while stack and price < stack[-1][1]:
                ans[stack[-1][0]] = time - stack[-1][0]
                stack.pop()
            stack.append((time, price))
        
        std_time = stack[-1][0]
        for time, price in stack:
            ans[time] = std_time - time
        
    return list(ans.values())