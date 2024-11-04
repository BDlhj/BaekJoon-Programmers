def solution(want, number, discount):
    answer = 0
    want_number = {product: quantity for product, quantity in zip(want, number)}
    
    for i in range(len(discount) - 9):
        want_number_copy = want_number.copy()
        for j in range(i, i + 10):
            if discount[j] in want:
                want_number_copy[discount[j]] -= 1
    
        for value in want_number_copy.values():
            if value > 0:
                break
        else:
             answer += 1
    
    return answer