import sys
input = sys.stdin.readline

width, height = map(int, input().split())
num_store = int(input())
store_locations = [list(map(int, input().split())) for _ in range(num_store)]
dg_direc, dg_dist = map(int, input().split())
answer = 0

for store_location in store_locations:
    st_direc, st_dist = store_location
    if st_direc == dg_direc:
        answer += abs(st_dist - dg_dist)
    else:
        if dg_direc == 1:
            if st_direc == 3:
                answer += dg_dist + st_dist
            elif st_direc == 4:
                answer += (width-dg_dist + st_dist)
            else:
                answer += (height + min(dg_dist+st_dist, (2*width-dg_dist-st_dist)))
        elif dg_direc == 2:
            if st_direc == 3:
                answer += dg_dist + (height - st_dist)
            elif st_direc == 4:
                answer += (width - dg_dist) + (height - st_dist)
            else:
                answer += (height + min(dg_dist+st_dist, (2*width-dg_dist-st_dist)))
        elif dg_direc == 3:
            if st_direc == 1:
                answer += dg_dist + st_dist
            elif st_direc == 2:
                answer += (height-dg_dist) + st_dist
            else:
                answer += (width + min(dg_dist+st_dist, (2*height-dg_dist-st_dist)))
        elif dg_direc == 4:
            if st_direc == 1:
                answer += dg_dist + (width - st_dist)
            elif st_direc == 2:
                answer += (height - dg_dist) + (width - st_dist)
            else:
                answer += (width + min(dg_dist + st_dist, (2 * height - dg_dist - st_dist)))

print(answer)
