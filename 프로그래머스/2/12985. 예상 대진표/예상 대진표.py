import math


def solution(n,a,b):
    round = 1
    while math.ceil(a/2) != math.ceil(b/2):
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        round += 1
    
    return round