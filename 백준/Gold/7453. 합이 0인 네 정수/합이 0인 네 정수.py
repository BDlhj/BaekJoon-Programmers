import sys
from collections import defaultdict, Counter
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
a = [num[0] for num in nums]
b = [num[1] for num in nums]
c = [num[2] for num in nums]
d = [num[3] for num in nums]

ab_sum = []
cd_sum = []

answer = 0

for i in range(n):
    for j in range(n):
        ab_sum.append(a[i]+b[j])
        cd_sum.append(c[i]+d[j])

cd_dict = Counter(cd_sum)

for num in ab_sum:
    answer += cd_dict[-num]

print(answer)