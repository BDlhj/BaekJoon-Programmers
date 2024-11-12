import math


def solution(n, stations, w):
    start, end = 0, 0
    apartments = []
    answer = 0
    
    for station in stations:
        start = station - w
        if start > end:
            apartments.append(start - end - 1)
        end = station + w
    
    if end < n:
        apartments.append(n - end)
        
    for apart in apartments:
        answer += math.ceil(apart / (2 * w + 1))
    
    return answer
    