import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
students = [0] * 12
answer = 0

for i in range(n):
    sex, grade = map(int, input().split())
    if sex == 0:
        students[grade-1] += 1
    if sex == 1:
        students[grade+5] += 1

for i in students:
    answer += (math.ceil(i/k))

print(answer)