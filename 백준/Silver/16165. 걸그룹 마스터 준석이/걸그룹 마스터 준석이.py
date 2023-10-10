import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
member_info = defaultdict(str)

for _ in range(n):
    group_name = input().rstrip()
    member_num = int(input())
    for _ in range(member_num):
        member_info[input().rstrip()] = group_name

for _ in range(m):
    quiz = input().rstrip()
    type = int(input())
    if type == 0:
        print('\n'.join(sorted([member[0] for member in member_info.items() if member[1] == quiz])))
    else:
        print(member_info[quiz])