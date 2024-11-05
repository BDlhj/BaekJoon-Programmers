def solution(nums):
    num_set = set(nums)
    choice_num = len(nums) / 2
    
    return choice_num if len(num_set) > choice_num else len(num_set)
