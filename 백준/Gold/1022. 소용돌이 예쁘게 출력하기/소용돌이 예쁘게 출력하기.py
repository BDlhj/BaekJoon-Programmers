import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
max_len = 0
answer = []

for r in range(r1, r2+1):
    pre_answer = []
    for c in range(c1, c2+1):
        if abs(r) >= abs(c):
            num = (abs(r) * 2 + 1) ** 2 - abs(r) * 4
            if r < 0:
                num -= (c - r)

            else:
                num += r * 2 + r + c
        else:
            num = (abs(c) * 2 + 1) ** 2 - abs(c) * 4
            if c < 0:
                num += (r - c)
            else:
                num -= c * 2 + c + r
        pre_answer.append(str(num))
    max_len = max(max_len, max(map(len, pre_answer)))
    answer.append(pre_answer)

for i in answer:
    for j in i:
        j = int(j)
        print(f'{j:{max_len}.0f}', end=' ')
    print()