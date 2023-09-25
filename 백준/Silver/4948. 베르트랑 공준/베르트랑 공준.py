import sys
from math import ceil
input = sys.stdin.readline

length = 123456
deleted = [False] * (length * 2 + 1)
deleted[1] = True

for i in range(2, ceil((length * 2 + 1)**(1/2))):
    if not deleted[i]:
        for j in range(2, (length * 2 + 1)//i+1):
            deleted[i*j] = True

while True:
    n = int(input())
    if n == 0:
        break
    
    answer = deleted[n+1:2*n+1].count(False)
    print(answer)