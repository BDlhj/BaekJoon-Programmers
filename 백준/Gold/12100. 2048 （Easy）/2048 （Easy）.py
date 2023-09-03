import sys
import copy
input = sys.stdin.readline

def move_up():
    for col in range(n):
        zero_exist = False
        for row in range(n):
            if graph[row][col] == 0 and not zero_exist:
                zero_row = row
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[zero_row][col] = graph[zero_row][col], graph[row][col]
                zero_row += 1

        for row in range(n):
            if row < n-1 and graph[row][col] == graph[row+1][col]:
                graph[row][col] *= 2
                graph[row+1][col] = 0
        
        zero_exist = False
        for row in range(n):
            if graph[row][col] == 0 and not zero_exist:
                zero_row = row
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[zero_row][col] = graph[zero_row][col], graph[row][col]
                zero_row += 1

def move_right():
    for row in range(n):
        zero_exist = False
        for col in range(n-1, -1, -1):
            if graph[row][col] == 0 and not zero_exist:
                zero_col = col
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[row][zero_col] = graph[row][zero_col], graph[row][col]
                zero_col -= 1

        for col in range(n-1, -1, -1):
            if col > 0 and graph[row][col] == graph[row][col-1]:
                graph[row][col] *= 2
                graph[row][col-1] = 0

        zero_exist = False
        for col in range(n-1, -1, -1):
            if graph[row][col] == 0 and not zero_exist:
                zero_col = col
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[row][zero_col] = graph[row][zero_col], graph[row][col]
                zero_col -= 1

def move_down():
    for col in range(n):
        zero_exist = False
        for row in range(n-1, -1, -1):
            if graph[row][col] == 0 and not zero_exist:
                zero_row = row
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[zero_row][col] = graph[zero_row][col], graph[row][col]
                zero_row -= 1

        for row in range(n-1, -1, -1):
            if row > 0 and graph[row][col] == graph[row-1][col]:
                graph[row][col] *= 2
                graph[row-1][col] = 0

        zero_exist = False
        for row in range(n-1, -1, -1):
            if graph[row][col] == 0 and not zero_exist:
                zero_row = row
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[zero_row][col] = graph[zero_row][col], graph[row][col]
                zero_row -= 1

def move_left():
    for row in range(n):
        zero_exist = False
        for col in range(n):
            if graph[row][col] == 0 and not zero_exist:
                zero_col = col
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[row][zero_col] = graph[row][zero_col], graph[row][col]
                zero_col += 1

        for col in range(n):
            if col < n-1 and graph[row][col] == graph[row][col+1]:
                graph[row][col] *= 2
                graph[row][col+1] = 0

        zero_exist = False
        for col in range(n):
            if graph[row][col] == 0 and not zero_exist:
                zero_col = col
                zero_exist = True
            if graph[row][col] > 0 and zero_exist:
                graph[row][col], graph[row][zero_col] = graph[row][zero_col], graph[row][col]
                zero_col += 1

# k번째에 어떻게 움직일 것인지
def backtrack(k):
    global graph, max_num

    if k == 5:
        max_num = max(max_num, max(list(map(max, graph))))
        return
    
    for i in range(4):
        graph_c = copy.deepcopy(graph)
        moves[i]()
        backtrack(k+1)
        graph = graph_c

# 판 크기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_num = -sys.maxsize # 최대 5번 이동해서 만들 수 있는 가장 큰 수
move_num = 5 # 최대 5번 이동
moves = {0: move_up, 1: move_right, 2: move_down, 3: move_left}

backtrack(0)
print(max_num)