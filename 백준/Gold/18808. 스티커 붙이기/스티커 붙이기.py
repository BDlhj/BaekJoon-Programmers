import sys
input = sys.stdin.readline

def attach_if_possible(row, col, heigth, width, attached):
    # 못 붙이는 경우
    for y in range(heigth):
        for x in range(width):
            if (row+y >= n or col+x >= m) or (sticker[y][x] == 1 and notebook[row+y][col+x] == 1):
                attached = False
                return attached
    
    # 붙일 수 있는 경우
    for y in range(height):
        for x in range(width):
            if sticker[y][x] == 1:
                notebook[row+y][col+x] = 1
    attached = True
    return attached

def rotate(sticker):
    new_sticker = [[0] * len(sticker) for _ in range(len(sticker[0]))]
    for row in range(len(new_sticker)):
        for col in range(len(new_sticker[0])):
            new_sticker[row][col] = sticker[len(new_sticker[0])-1-col][row]

    sticker = new_sticker
    
    return sticker

# 세로 길이, 가로 길이, 스티커 개수
n, m, k = map(int, input().split())

# 스티커 모양 정보를 담은 딕셔너리
stickers = []
notebook = [[0] * m for _ in range(n)]
answer = 0

# stickers에 스티커 모양 추가
for i in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)

for sticker in stickers:
    attached = False
    rotate_cnt = 0
    while rotate_cnt < 4:
        height = len(sticker)
        width = len(sticker[0])
        for row in range(n):
            for col in range(m):
                attached = attach_if_possible(row, col, height, width, attached)
                if attached:
                    break
            if attached:
                break
        
        # 붙였으면 다음 스티커로 넘어가기
        if attached:
            break

        # 못 붙였으면 돌리기
        sticker = rotate(sticker)
        rotate_cnt += 1

for line in notebook:
    answer += line.count(1)

print(answer)