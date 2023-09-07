import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
done = False
answer = 0

def clean(r, c, d):
    global answer, done

    if board[r][c] == 0:
        board[r][c] = -1
        answer += 1

    # 네 방향 중 청소된 곳 개수 확인
    cleaned_cnt = 0
    for i in range(4):
        if board[r+dy[i]][c+dx[i]] != 0:
            cleaned_cnt += 1
    
    # 네 방향 중 청소할 수 있는 곳이 없을 때
    if cleaned_cnt == 4:
        # 후진할 수 없으면 종료
        if board[r+dy[(d+2)%4]][c+dx[(d+2)%4]] == 1:
            done = True
            return
        # 후진할 수 있으면 방향 유지한 채로 후진
        clean(r+dy[(d+2)%4], c+dx[(d+2)%4], d)
        if done:
            return
    
    # 네 방향 중 청소할 수 있는 곳이 있을 때
    else:
        d_i = d
        while cleaned_cnt < 4:
            d_i = (d_i - 1) % 4
            if board[r+dy[d_i]][c+dx[d_i]] == 0:
                cleaned_cnt += 1
                clean(r+dy[d_i], c+dx[d_i], d_i)
                if done:
                    return

clean(r, c, d)
print(answer)