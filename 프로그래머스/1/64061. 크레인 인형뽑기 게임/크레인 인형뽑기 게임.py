def solution(board, moves):
    board = list(zip(*board))
    board = [list(line)[::-1] for line in board]
    for line in board:
        for j in line[::-1]:
            if j == 0:
                line.pop()

    stack = []
    ans = 0

    for move in moves:
        move -= 1
        if board[move]:
            if not stack:
                stack.append(board[move].pop())
            else:
                if stack[-1] == board[move][-1]:
                    stack.pop()
                    board[move].pop()
                    ans += 2
                else:
                    stack.append(board[move].pop())
            
    return ans
