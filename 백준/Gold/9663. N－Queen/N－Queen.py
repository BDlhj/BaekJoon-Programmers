import sys
input = sys.stdin.readline

n = int(input())
answer = 0
placed = []

def backtrack(row):
    global answer, n
    already_set = False

    if len(placed) == n:
        answer += 1
        return

    for col in range(n):
        for pos in placed:
            if col == pos[1] or abs(row - pos[0]) == abs(col - pos[1]): 
                already_set = True
                break
        if already_set:
            already_set = False
            continue
        placed.append((row, col))
        backtrack(row+1)
        placed.pop()

backtrack(0)

print(answer)