import sys
input = sys.stdin.readline

d = [(-1,0),(0,1),(1,0),(0,-1)]
def match(cnt,r,c):
    global result
    result = max(result,cnt)
    for i in range(4):
        dr, dc = d[i]
        row = r + dr
        col = c + dc
        if 0 <= row < R and 0 <= col < C and not arr[row][col] in alpha_set:
            alpha_set.add(arr[row][col])
            match(cnt+1,row,col)
            alpha_set.remove(arr[row][col])

R, C = map(int,input().split())
arr = [list(map(lambda x: ord(x)-65,input().strip())) for _ in range(R)]
result = 0
alpha_set = set()
alpha_set.add(arr[0][0])
match(1,0,0)
print(result)