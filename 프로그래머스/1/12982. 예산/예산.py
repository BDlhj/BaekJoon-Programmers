def solution(d, budget):
    d.sort()
    sum_, result = 0, 0
    
    for i in d:
        if sum_ + i <= budget:
            sum_ += i
            result += 1
    
    return result