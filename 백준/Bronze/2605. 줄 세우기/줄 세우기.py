import sys
input = sys.stdin.readline

num_of_students = int(input())
numbers = list(map(int, input().split()))
line = []

for student in range(1, num_of_students+1):
    if not line:
        line.append(student)
    else:
        sub = []
        for _ in range(numbers[student-1]):
            sub.append(line.pop())
        line.append(student)
        for _ in range(numbers[student-1]):
            line.append(sub.pop())
print(*line)
