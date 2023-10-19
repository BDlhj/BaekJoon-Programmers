import sys
from collections import defaultdict
input = sys.stdin.readline

tree_dict = defaultdict(int)
cnt = 0
while True:
    tree = input().rstrip()
    if tree == '':
        break
    tree_dict[tree] += 1
    cnt += 1

for i in sorted(tree_dict.items()):
    print(f'{i[0]}{i[1]/cnt * 100: .4f}')