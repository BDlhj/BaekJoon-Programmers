import sys
input = sys.stdin.readline

TC = 4
for _ in range(TC):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 점
    if ((x1, y1) == (p2, q2)) or ((x2, y2) == (p1, q1))\
            or ((x1, q1) == (p2, y2)) or ((p1, y1) == (x2, q2)):
        print('c')
    # 없음
    elif (p1 < x2) or (q1 < y2) or (p2 < x1) or (q2 < y1):
        print('d')
    # 선분
    elif (q1 == y2 and (p2 > x1 and x2 < p1)) \
            or (p1 == x2 and (y2 < q1 and q2 > y1))\
            or (x1 == p2 and (y2 < q1 and q2 > y1))\
            or (y1 == q2 and (p2 > x1 and x2 < p1)):
        print('b')
    else:
        print('a')

