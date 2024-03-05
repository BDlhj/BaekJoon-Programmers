def chess_cnt(tmp,r,c,r_s,c_s):
    global min_cnt, cnt, loc
    if loc > 63:
        if min_cnt > cnt:
            min_cnt = cnt
    else:
        loc += 1
        item = chess[r+r_s][c+c_s]
        if tmp == item:
            cnt += 1
            if item == 'B':
                tmp = 'W'
            else:
                tmp = 'B'
        else:
            tmp = item
        if r%2:
            if c > 0:
                chess_cnt(tmp,r,c-1,r_s,c_s)
            else:
                chess_cnt(tmp,r+1,c,r_s,c_s)
        else:
            if c < 7:
                chess_cnt(tmp,r,c+1,r_s,c_s)
            else:
                chess_cnt(tmp,r+1,c,r_s,c_s)




N,M = map(int,input().split())
chess = [input() for _ in range(N)]
min_cnt = 64
for i in range(M-7):
    for j in range(N-7):
        for k in ['B','W']:
            cnt = 0
            loc = 0
            chess_cnt(k,0,0,j,i)
print(min_cnt)