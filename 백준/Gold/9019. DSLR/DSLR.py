import sys
from collections import deque
input = sys.stdin.readline


def D(num):
    return 2*num % 10000


def S(num):
    return (num - 1) % 10000


def L(num):
    return (num % 1000)*10 + num//1000


def R(num):
    return num//10 + (num % 10)*1000


funcs = [D, S, L, R]

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    nums = ["" for _ in range(10000)]
    visited = [False] * 10000
    q = deque()
    q.append(A)
    visited[A] = True
    done = False
    answer = []

    while q:
        c_num = q.popleft()
        for func in funcs:
            next_num = func(c_num)
            if next_num == B:
                print(''.join([nums[c_num], f'{func.__name__}']))
                done = True
                break
            if not visited[next_num]:
                nums[next_num] = nums[c_num] + f'{func.__name__}'
                q.append(next_num)
                visited[next_num] = True
        if done:
            break
