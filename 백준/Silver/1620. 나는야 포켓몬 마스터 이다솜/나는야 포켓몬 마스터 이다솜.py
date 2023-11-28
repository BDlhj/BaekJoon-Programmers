import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
dic_str_to_int = defaultdict(int)
dic_int_to_str = defaultdict(str)

for i in range(1, n+1):
    name = input().rstrip()
    dic_str_to_int[name] = i
    dic_int_to_str[str(i)] = name

for _ in range(m):
    t = input().rstrip()
    if t.isalpha():
        print(dic_str_to_int[t])
    else:
        print(dic_int_to_str[t])
