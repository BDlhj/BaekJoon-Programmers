def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        share, rest = divmod(i, n)
        
        if share >= rest:
            answer.append(share + 1)
        else:
            answer.append(rest + 1)
                
    return answer
        