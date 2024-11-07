def solution(keyinput, board):
    width = (board[0] - 1) // 2
    height = (board[1] - 1) // 2
    
    move = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    cx, cy = 0, 0
    
    for key_ in keyinput:
        dx, dy = move[key_]
        if (-height <= cy + dy <= height) and (-width <= cx + dx <= width):
            cy += dy
            cx += dx
    
    return [cx, cy]