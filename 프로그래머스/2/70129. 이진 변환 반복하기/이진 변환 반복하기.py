def make_binary(num):
    result = []
    while num > 1:
        result.append(str(num % 2))
        num //= 2
    result.append(str(num))
    
    return ''.join(result[::-1])

def solution(s):
    answer = [0, 0]
    
    while s != '1':
        answer[1] += s.count('0')
        s = s.replace('0', '')
        
        n = len(s)
        s = make_binary(n)
        answer[0] += 1
    
    return answer