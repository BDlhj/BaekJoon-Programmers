def solution(triangle):
    for row in range(len(triangle) - 1, 0, -1):
        for col in range(len(triangle[row]) - 1):
            triangle[row - 1][col] = max(triangle[row - 1][col] + triangle[row][col], triangle[row - 1][col] + triangle[row][col + 1])
    
    return triangle[0][0]