def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    s.sort(key=lambda x: len(x))
    
    for set_ in s:
        nums = set_.split(',')
        for num in nums:
            if int(num) not in answer:
                answer.append(int(num))
    
    return answer