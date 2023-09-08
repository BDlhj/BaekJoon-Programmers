import sys
input = sys.stdin.readline

def type1():
    figure = type_1
    for _ in range(2):
        for r in range(n):
            for c in range(m):
                if r+len(figure)-1 < n and c+len(figure[0])-1 < m:
                    cal_max_sum(figure, r, c)
        figure = rotate_figure(figure)

def type2():
    figure = type_2
    for r in range(n):
        for c in range(m):
            if r+len(figure)-1 < n and c+len(figure[0])-1 < m:
                cal_max_sum(figure, r, c)

def type345():
    for figure in types[2:]:
        for _ in range(4):
            for _ in range(2):
                for r in range(n):
                    for c in range(m):
                        if r+len(figure)-1 < n and c+len(figure[0])-1 < m:
                            cal_max_sum(figure, r, c)
                figure = flip_figure(figure)
                cal_max_sum(figure, r, c)
            figure = rotate_figure(figure)

def cal_max_sum(figure, r, c):
    global max_sum
    sub_sum = 0

    for row in range(len(figure)):
        for col in range(len(figure[0])):
            if figure[row][col] and (r+row < n and c+col < m):
                sub_sum += paper[r+row][c+col]

    max_sum = max(max_sum, sub_sum)

def rotate_figure(figure):
    new_figure = [[0] * len(figure) for _ in range(len(figure[0]))]
    for row in range(len(new_figure)):
        for col in range(len(new_figure[0])):
            new_figure[row][col] = figure[len(new_figure[0])-1-col][row]
    return new_figure

def flip_figure(figure):
    new_figure = [[0] * len(figure[0]) for _ in range(len(figure))]
    for row in range(len(new_figure)):
        for col in range(len(new_figure[0])):
            new_figure[row][col] = figure[row][len(new_figure[0])-1-col]
    return new_figure

# 세로, 가로
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
max_sum = 0

type_1 = [[1, 1, 1, 1]]
type_2 = [[1] * 2 for _ in range(2)]
type_3 = [[1] * 3 for _ in range(2)]
type_4 = [[1] * 3 for _ in range(2)]
type_5 = [[1] * 3 for _ in range(2)]

type_3[1][1] = 0
type_3[1][2] = 0

type_4[0][0] = 0
type_4[1][2] = 0

type_5[1][0] = 0
type_5[1][2] = 0

types = [type_1, type_2, type_3, type_4, type_5]
type1()
type2()
type345()

print(max_sum)