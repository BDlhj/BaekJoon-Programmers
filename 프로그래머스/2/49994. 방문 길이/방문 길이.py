def solution(dirs):
    move = {
        'U': [1, 0],
        'D': [-1, 0],
        'R': [0, 1],
        'L': [0, -1]
    }
    
    r, c = 0, 0
    history = []
    
    for dir in dirs:
        dr, dc = move[dir]
        if not ((-5 <= r + dr <= 5) and (-5 <= c + dc <= 5)):
            continue

        new_r, new_c = r + dr, c + dc        
        diff = sorted([[r, c], [new_r, new_c]])
        if diff not in history:
            history.append(diff)
        r, c = new_r, new_c

    return len(history)