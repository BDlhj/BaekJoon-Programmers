import itertools

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def solution(nums):
    result = 0
    comb_list = list(itertools.combinations(nums, 3))
    sum_list = [sum(comb) for comb in comb_list]

    for num in sum_list:
        if is_prime(num):
            result += 1
    
    return result