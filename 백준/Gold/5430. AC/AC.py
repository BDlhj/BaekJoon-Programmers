import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    input_list = eval(input())
    is_error = False
    is_empty = False if n > 0 else True
    s_i, e_i = 0, n - 1

    for f in p:
        if f == 'D':
            if is_empty:
                print('error')
                is_error = True
                break
            elif s_i == e_i:
                s_i, e_i = 0, -sys.maxsize
                is_empty = True
            elif s_i < e_i:
                s_i += 1
            elif s_i > e_i:
                s_i -= 1
        if f == 'R':
            s_i, e_i = e_i, s_i

    if is_empty and not is_error:
        print([])
    if not is_empty and not is_error:
        if s_i > e_i:
            if e_i == 0:
                answer = input_list[s_i::-1]
            else:
                answer = input_list[s_i:e_i-1:-1]
        else:
            answer = input_list[s_i:e_i+1]

        print('['+','.join(list(map(str, answer)))+']')