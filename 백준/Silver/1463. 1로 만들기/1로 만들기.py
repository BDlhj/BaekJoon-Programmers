import sys
input = sys.stdin.readline

num = int(input())
min_num = [0] * (num+1)

for i in range(2, num+1):
    min_num[i] = min_num[i-1] + 1
    if i % 2 == 0:
        min_num[i] = min(min_num[i], min_num[i//2] + 1)
    if i % 3 == 0:
        min_num[i] = min(min_num[i], min_num[i//3] + 1)

print(min_num[num])