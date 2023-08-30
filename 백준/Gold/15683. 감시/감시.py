import sys
import copy
input = sys.stdin.readline

def first_right(row, col):
    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break
        
def first_down(row, col):
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break

def first_left(row, col):
    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break

def first_up(row, col):
    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break

def second_width(row, col):
    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break
    
    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break

def second_height(row, col):
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break
    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break


def third_right(row, col):
    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break

    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break
    
def third_down(row, col):
    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break
    
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break

def third_left(row, col):
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break

    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break

def third_up(row, col):
    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break
    
    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break


def fourth_right(row, col):
    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break
        
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break

    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break

def fourth_down(row, col):
    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break
        
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break

    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break

def fourth_left(row, col):
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break

    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break

    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break

def fourth_up(row, col):
    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break

    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break

    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break


def fifth(row, col):
    for x in range(col+1, m):
        if graph[row][x] == 0:
            graph[row][x] = -1 
        if graph[row][x] == 6:
            break
        
    for y in range(row+1, n):
        if graph[y][col] == 0:
            graph[y][col] = -1 
        if graph[y][col] == 6:
            break

    for x in range(col, -1, -1):
        if graph[row][x] == 0:
            graph[row][x] = -1
        if graph[row][x] == 6:
            break

    for y in range(row, -1, -1):
        if graph[y][col] == 0:
            graph[y][col] = -1
        if graph[y][col] == 6:
            break


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctv_locs = []
cnt = 0
min_v = sys.maxsize
direction_num = {'0': 0, '1': 4, '2': 2, '3': 4, '4': 4, '5': 1}
check_funcs = {
    0: 0,
    1: {
        0: first_right,
        1: first_down,
        2: first_left,
        3: first_up
    },
    2: {
        0: second_width,
        1: second_height
    },
    3: {
        0: third_right,
        1: third_down,
        2: third_left,
        3: third_up
    },
    4: {
        0: fourth_right,
        1: fourth_down,
        2: fourth_left,
        3: fourth_up
    },
    5: {
        0: fifth
    }
}

for row in range(n):
    for col in range(m):
        if 1 <= graph[row][col] <= 5:
            cctv_locs.append((cnt, graph[row][col], row, col))
            cnt += 1
cctv_locs.append((0, 0, 0, 0))

def backtrack(num, type, row, col):
    global min_v, graph
    if num == cnt:
        unseen = 0
        for i in graph:
            unseen += i.count(0)
        min_v = min(min_v, unseen)
        return
    
    for i in range(direction_num[str(type)]):
        graph_copy = copy.deepcopy(graph)
        check_funcs[type][i](row, col)
        backtrack(num+1, cctv_locs[num+1][1], cctv_locs[num+1][2], cctv_locs[num+1][3])
        graph = graph_copy

backtrack(0, cctv_locs[0][1], cctv_locs[0][2], cctv_locs[0][3])
print(min_v)