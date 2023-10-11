import sys
from collections import defaultdict
input = sys.stdin.readline

s = input().rstrip()
len_s = len(s)
d = defaultdict(int)

for length in range(1, len_s+1):
    s_idx = 0
    for _ in range(len_s):
        partial_str = s[s_idx:s_idx+length]
        d[partial_str] = 1
        s_idx += 1

print(len(d))