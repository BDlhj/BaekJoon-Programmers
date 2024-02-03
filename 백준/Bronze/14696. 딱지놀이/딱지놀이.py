import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a_nums = list(map(int, input().split()))[1:]
    b_nums = list(map(int, input().split()))[1:]
    a_count = defaultdict(int, Counter(a_nums))
    b_count = defaultdict(int, Counter(b_nums))

    for i in range(4, 0, -1):
        if a_count[i] > b_count[i]:
            print('A')
            break
        elif a_count[i] < b_count[i]:
            print('B')
            break
    else:
        print('D')
