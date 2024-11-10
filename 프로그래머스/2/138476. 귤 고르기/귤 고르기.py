from collections import Counter


def solution(k, tangerine):
    answer = 0
    tangerine_count = list(Counter(tangerine).items())
    tangerine_count.sort(key=lambda x: x[1], reverse=True)
    
    for tangerine in tangerine_count:
        if k:
            if tangerine[1] <= k:
                answer += 1
                k -= tangerine[1]
            else:
                answer += 1
                break
        else:
            break
    
    return answer