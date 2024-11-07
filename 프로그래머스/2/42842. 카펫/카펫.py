def solution(brown, yellow):
    answer = [0, 0]
    brown = (brown - 4) // 2
    
    for row in range(1, brown):
        col = brown - row
        if row * col == yellow:
            answer = [row + 2, col + 2]
    
    return answer