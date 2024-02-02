import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_dist = p + t
y_dist = q + t
x_reflect_time, x_loc = divmod(x_dist, w)
y_reflect_time, y_loc = divmod(y_dist, h)

final_x = x_loc if not x_reflect_time % 2 else (w-x_loc)
final_y = y_loc if not y_reflect_time % 2 else (h-y_loc)

print(final_x, final_y)
